import simpleaudio as sa


def order_placed():
    # Load the sound file
    wave_obj = sa.WaveObject.from_wave_file('../audio/reminders.wav')

    # Play the sound file
    play_obj = wave_obj.play()

    # Wait for the sound to finish playing
    # play_obj.wait_done()
    # print('played')


