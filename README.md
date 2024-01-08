<h1 style="margin: auto; width: 100%; text-align: center; font-size: 25px;">Jazz/Classical Dataset Download</h1>

Given a list of YouTube links to jazz and classical audio, downloads a dataset of five-second WAV files for training an audio classifier

Packages required: pytube, moviepy, pydub (install with pip)

<a href="#">See sample dataset on Kaggle</a>

------------------------------

<h2>Parameters:</h2>
- LENGTH_OF_CLIP: Length (in milliseconds) of each audio sample

- NUMBER_OF_CLIPS: Total number of clips in dataset. Evenly split between jazz and classical samples

- BASE_PATH: Path to directory where dataset folder will be created

- classical_clips: A list of nested two element lists (representing a YouTube audio sample), where...
	- clip[0]: YouTube link (string)
	- clip[1]: Desired filename (string)

- jazz_clips: A list of nested two element lists (representing a YouTube audio sample), where...
	- clip[0]: YouTube link (string)
	- clip[1]: Desired filename (string)

------------------------------

<h2>Methods:</h2>

download_and_split(path, n_clips_per_link, list_of_clips): Downloads each audio sample as <i>n</i> WAV files
- path: Desired path for .WAV files to be downloaded and produced
- n_clips_per_link: Number of .wav clips to be produced from each downloaded .mp4 file
- list_of_clips: A list of nested two element lists (representing a YouTube audio sample), where...
	- clip[0]: YouTube link (string)
	- clip[1]: Desired filename (string)

download(clip, path): Downloads a YouTube link as an MP4 file
- clip: A two-item list representing a YouTube audio sample, where...
	- clip[0]: YouTube link (string)
	- clip[1]: Desired filename (string)
- path: Desired path for YouTube video

split_mp4_into_wavs(path, n_clips, length=LENGTH_OF_CLIP): Splits an MP4 file into <i>n</i> WAV files, taken from even increments throughout the song
- path: Path to .mp4 file
- n_clips: Number of .wav clips to be produced from .mp4 file
- length: Length of each respective clip (defaults to LENGTH_OF_CLIP parameter)
init_directories(path=BASE_PATH): Writes a 'dataset' directory with subdirectories 'Classical' and 'Jazz'
- path: Path for 'dataset' (defaults to BASE_PATH)

-------------------------------

<b>Installation is easy!</b> Download and run script in .py or .ipynb format
