from .youtube_json3_schema import validate_youtube_cc_json3
from .logger import logger

from typing import Union, Optional, NamedTuple, List

import json
import pandas as pd
from pathlib import Path


class LineCC(NamedTuple):
    event_id: int
    start_time_ms: int
    duration_ms: int
    window_id: int
    window_style_id: int
    window_position_id: int
    append: bool
    segments: List[str]


class YoutubeCC:

    _LINES_FIELDS_MAP = {
        "event_id": "id",
        "start_time_ms": "tStartMs",
        "duration_ms": "dDurationMs",
        "window_id": "wWinId",
        "window_style_id": "wsWinStyleId",
        "window_position_id": "wpWinPosId",
        "append": "aAppend",
    }

    _SEGMENTS_FIELDS_MAP = {
        "text": "utf8",  # UTF-8 text of the segment
        "asr_confidence": "acAsrConf",  # Automatic Speech Recognition confidence
        "offset_ms": "tOffsetMs",  # Offset from the start of the event
        "pen_id": "pPenId",  # Pen ID
    }

    def __init__(self, file_path: Union[Path, str]):

        self.file_path = file_path if isinstance(file_path, Path) else Path(file_path)
        self.file_path = self.file_path.resolve()
        if not self.file_path.exists():
            logger.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")

        self.lines_df = pd.DataFrame()
        self.segments_df = pd.DataFrame()
        self.load_json3()

    def load_json3(self):
        """Load captions from a JSON3 file and initialize DataFrames."""
        with open(self.file_path, "r") as file:
            data = json.load(file)

        if not validate_youtube_cc_json3(data):
            logger.error("Unexpected JSON3 format.")
            raise ValueError("Invalid Youtube CC JSON3 file")

        line_rows = {field: [] for field in self._LINES_FIELDS_MAP.keys()}
        segment_rows = {
            field: []
            for field in list(self._SEGMENTS_FIELDS_MAP.keys())
            + ["start_time_ms", "line_id"]
        }

        for line_id, line in enumerate(data["events"]):

            for df_field, pb3_field in self._LINES_FIELDS_MAP.items():
                line_rows[df_field].append(line.get(pb3_field, None))

            event_start_time_ms = line.get("tStartMs", None)
            for seg in line.get("segs", []):
                for df_field, pb3_field in self._SEGMENTS_FIELDS_MAP.items():
                    segment_rows[df_field].append(seg.get(pb3_field, None))

                segment_rows["start_time_ms"].append(
                    None
                    if (event_start_time_ms is None)
                    else event_start_time_ms + seg.get("tOffsetMs", 0)
                )
                segment_rows["line_id"].append(line_id)

        self._lines_df = pd.DataFrame(line_rows)
        self._segments_df = pd.DataFrame(segment_rows)

    @property
    def lines(self):
        """Return a copy of the DataFrame containing all the lines."""
        return self._lines_df.copy()

    @property
    def segments(self):
        """Return a copy of the DataFrame containing all the segments."""
        return self._segments_df.copy()

    def __repr__(self):
        return f"YoutubeCC(file={self.file_path}, lines={len(self._lines_df)}, segments={len(self._segments_df)})"

    def _repr_html_(self):
        return f"""
        <h3>YoutubeCC</h3>
        <ul>
            <li>File: {self.file_path}</li>
            <li>lines: {len(self._lines_df)}</li>
            <li>Segments: {len(self._segments_df)}</li>
        </ul>
        """

    def __str__(self) -> str:
        return f"YoutubeCC(file={self.file_path}, lines={len(self._lines_df)}, segments={len(self._segments_df)})"

    def __len__(self) -> int:
        return len(self._lines_df)

    def __getitem__(self, key):
        line_row = self._lines_df.iloc[key]
        line_cc = LineCC(
            event_id=line_row["event_id"],
            start_time_ms=line_row["start_time_ms"],
            duration_ms=line_row["duration_ms"],
            window_id=line_row["window_id"],
            window_style_id=line_row["window_style_id"],
            window_position_id=line_row["window_position_id"],
            append=line_row["append"],
            segments=self._segments_df[
                self._segments_df["line_id"] == key
            ].text.tolist(),
        )
        return line_cc
    
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def get_text(
        self, start_time_ms: int = 0, end_time_ms: Optional[int] = None
    ) -> str:
        """Return the text of the segments between start_time_ms and end_time_ms.

        Args:
            start_time_ms (int): Start time in milliseconds.
            end_time_ms (int, optional): End time in milliseconds. Defaults to None.

        Returns:
            str: Concatenated text of the segments.
        """
        mask = start_time_ms <= self._segments_df["start_time_ms"]
        if end_time_ms is not None:
            mask &= self._segments_df["start_time_ms"] < end_time_ms
        return "".join(self._segments_df[mask].text.tolist())
