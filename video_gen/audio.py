from pydub import AudioSegment

def get_position(track, signal):
    return (len(track)-len(signal))/2

def add_signal(track_filename, signal_filename, position = None):
    track = AudioSegment.from_file(track_filename)
    signal = AudioSegment.from_file(signal_filename)
    if not position:
        position = get_position(track, signal)
    track_overlayed = track.overlay(signal, position = position)
    fname, format = track_filename.split('.')
    output_filename = fname+'_overlayed.'+format
    track_overlayed.export(output_filename, format = format, bitrate = track.frame_rate)
    return output_filename

# track_filename = 'samples/ad1_audio.wav'
# signal_filename = 'samples/signal_16950Hz_44100fps_5s.wav'
# position = 3000
# add_signal(track_filename, signal_filename, position)