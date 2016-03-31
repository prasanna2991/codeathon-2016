import make_signal
import audio
import video

# variables for the signals' audio files

duration = 5 # duration in seconds
frequencies = [24000]
bitrate = 44100.0

position = 5000 # starting position in milliseconds in the ad where the signal will be added

samples_folder = 'samples'
input_ads = ['ad1.mp4']

def main():
    make_signal.generate_files(samples_folder, frequencies, duration, bitrate)
    signal_filename = make_signal.get_filename(samples_folder, frequencies[0], duration, bitrate)
    video_filename = samples_folder+'/'+input_ads[0]
    video_part_filename = video.get_video_part(video_filename)
    track_filename = video.get_audio_part(video_filename)
    audio_part_with_signal_filename = audio.add_signal(track_filename, signal_filename, position)
    video.get_video(video_part_filename, audio_part_with_signal_filename)

main()
