# Audio Bandpass Filtering Script

This Python script applies a bandpass Butterworth filter to an input WAV audio file, isolating frequencies between 300 Hz and 3400 Hz — a common range for human speech. The filtered audio is saved as a new WAV file, and waveform plots are generated for visual comparison.

## Features
- Reads a WAV audio file (`speech_input.wav`)
- Applies a zero-phase Butterworth bandpass filter (6th order)
- Normalizes audio data for stable filtering
- Saves filtered audio as `filtered_output.wav`
- Generates and saves waveform plots:
  - Original audio waveform
  - Filtered audio waveform
  - Overlay of original and filtered waveforms

## Requirements
- Python
- NumPy
- SciPy
- Matplotlib

## Usage
1. Place the input WAV file named `speech_input.wav` in the same directory as the script.
2. Run the script

3. The script will generate:
   - `filtered_output.wav` — filtered audio file
   - `original_audio.png` — plot of original waveform
   - `filtered_audio.png` — plot of filtered waveform
   - `original_vs_filtered.png` — overlay plot comparing original and filtered signals

## Parameters to modify
- `lowcut`: Low cutoff frequency in Hz (default 300)
- `highcut`: High cutoff frequency in Hz (default 3400)
- `order`: Filter order (default 6)
- Input and output filenames

## Notes
- Designed primarily for speech signals.
- Uses zero-phase filtering to avoid phase distortion.
- Normalization ensures no clipping in output audio.

---




