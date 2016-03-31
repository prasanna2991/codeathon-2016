from subprocess import Popen, PIPE

def run_shell_command(command):
    proc = Popen(command, stdout=PIPE, shell=True, bufsize=1)
    lines = tuple(line.strip() for line in proc.stdout)
    return lines

def get_video_part_filename(video_filename):
    fname, format = video_filename.split('.')
    return fname+'_silent.'+format

def get_video_part(video_filename):
    video_part_filename = get_video_part_filename(video_filename)
    command = ' '.join(['ffmpeg', '-i', video_filename, '-c', 'copy', '-an', '-y', video_part_filename])
    run_shell_command(command)
    return video_part_filename

def get_audio_part_filename(video_filename):
    fname, format = video_filename.split('.')
    return fname+'_audio.wav'

def get_audio_part(video_filename):
    audio_part_filename = get_audio_part_filename(video_filename)
    command = ' '.join(['ffmpeg', '-i', video_filename, '-vn', '-acodec', 'pcm_u8', '-y', audio_part_filename])
    run_shell_command(command)
    return audio_part_filename

def get_video_filename(video_part_filename):
    fname, format = video_part_filename.split('.')
    return fname.replace('_silent', '_final')+'.'+format

def get_video(video_part_filename, audio_part_filename):
    video_filename = get_video_filename(video_part_filename)
    command = ' '.join(['ffmpeg', '-i', video_part_filename, '-i', audio_part_filename, '-c:v', 'copy', '-c:a', 'aac', '-y', video_filename])
    run_shell_command(command)
    return video_filename