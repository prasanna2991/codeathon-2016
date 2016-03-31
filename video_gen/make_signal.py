import math
import wave
import struct

def generate_wav(filename, frequency, duration, bitrate, amplitude = 64000.0):
    frames = int(bitrate*duration)
    sine_list = [math.sin(2*math.pi*frequency*(x/bitrate)) for x in range(frames)]
    wav_file = wave.open(filename, "w")

    nchannels = 2
    sampwidth = 2
    framerate = int(bitrate)
    nframes = frames
    comptype = "NONE"
    compname = "not compressed"

    wav_file.setparams((nchannels, sampwidth, framerate, nframes,
                        comptype, compname))
    for s in sine_list:
        # write the audio frames to file
        wav_file.writeframes(struct.pack('h', int(s * amplitude / 2)))
        wav_file.writeframes(struct.pack('h', int(s * amplitude / 2)))
    wav_file.close()

def get_filename(folder, freq, duration, bitrate):
    filename_pattern = "{folder}/signal_{freq}Hz_{bitrate}fps_{duration}s.wav"
    filename = filename_pattern.format(folder = folder, freq = freq, bitrate = int(bitrate), duration = duration)
    return filename

def generate_files(folder, frequencies, duration, bitrate):
    for freq in frequencies:
        filename = get_filename(folder, freq, duration, bitrate)
        generate_wav(filename, freq, duration, bitrate)

duration = 5
frequencies = [16950]
bitrate = 44100.0

samples_folder = 'samples'
generate_files(samples_folder, frequencies, duration, bitrate)