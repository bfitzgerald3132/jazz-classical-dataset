from pytube import YouTube
from moviepy import editor as mp
from matplotlib import pyplot as plt
from pydub import AudioSegment
import wave
import numpy as np
import os
import random

# Define parameters
LENGTH_OF_CLIP = 5000
NUMBER_OF_CLIPS = 1500
BASE_PATH = "TODO ADD PATH" # Omit terminating slash

# Define clips
classical_clips = [
    ["https://www.youtube.com/watch?v=t3217H8JppI", "beethoven_a"],
    ["https://www.youtube.com/watch?v=0Ak_7tTxZrk", "beethoven_b"],
    ["https://www.youtube.com/watch?v=qcuaN3jN29Q", "verdi"],
    ["https://www.youtube.com/watch?v=SVnF3x44rvU", "tchaikovsky"],
    ["https://www.youtube.com/watch?v=JH3T6YwwU9s", "handel"],
    ["https://www.youtube.com/watch?v=3FLbiDrn8IE", "bach"],
    ["https://www.youtube.com/watch?v=Hk0rWMWHLA4", "wagner"],
    ["https://www.youtube.com/watch?v=PK92oCLrOag", "mozart"],
    ["https://www.youtube.com/watch?v=rP42C-4zL3w", "stravinasky"], #rite of spring
    ["https://www.youtube.com/watch?v=Qut5e3OfCvg", "dvorak"], #new world
    ["https://www.youtube.com/watch?v=wh1Ky7gj4vw", "schubert"], #winterreise
    ["https://www.youtube.com/watch?v=tUe-clNbnBE", "brahms"], #hungarian dances
    ["https://www.youtube.com/watch?v=Ynky7qoPnUU", "schumann"], # op. 54
    ["https://www.youtube.com/watch?v=SEkcP8lZvZA", "mendelssohn"], #op. 21
    ["https://www.youtube.com/watch?v=O31KPk5xnBg", "mussorgsky"], #pictures at exhibition
    ["https://www.youtube.com/watch?v=9E6b3swbnWg", "chopin"], #op 9
    ["https://www.youtube.com/watch?v=buw9zpwSg7M", "berlioz"], # h 48
    ["https://www.youtube.com/watch?v=H_1OtRt0_ho", "puccini"], # la boheme
    ["https://www.youtube.com/watch?v=IeKMMDxrsBE", "liszt"], # s. 178
    #["https://www.youtube.com/watch?v=GRxofEmo3HA", "vivaldi"], # four seasons
    ["https://www.youtube.com/watch?v=IFPwm0e_K98", "strauss_r"], # also sprach zarathurstra
    ["https://www.youtube.com/watch?v=vOvXhyldUko", "mahler_g"], # ORCHESTRA TUNES AT BEGINNING. no 5
    ["https://www.youtube.com/watch?v=iXU8EXL7a_4", "sibelius_j"], # op 43
    ["https://www.youtube.com/watch?v=UnilUPXmipM", "faure"], # requiem d minor
    ["https://www.youtube.com/watch?v=rEGOihjqO9w", "rachmaninoff"], #op 18
    ["https://www.youtube.com/watch?v=A12T7kra0Eo", "debussy"], #la mer
    ["https://www.youtube.com/watch?v=I1Yoyz6_Los", "grieg_e"], # op 16
    ["https://www.youtube.com/watch?v=fSJwP5dvzPg", "shostakovich"], # op 93
    ["https://www.youtube.com/watch?v=-LGjLBzAhKw", "copland_a"], # Appalachian spring
    ["https://www.youtube.com/watch?v=eFccAm9C8hk", "bizet"], #carmen orchestrial suite
    ["https://www.youtube.com/watch?v=17lEx0ytE_0", "rimsky_korsakov"], # scheherazade, op 35
    ["https://www.youtube.com/watch?v=BRfF7W4El60", "palestrina"], # missa papae marcelli
    ["https://www.youtube.com/watch?v=FFQ00FHVSGg", "bruckner_a"], # wab 107
    ["https://www.youtube.com/watch?v=9uwpuyc7nS4", "bartok"], # concerto for orchestra, bb 123
]
# Taken (mostly) from https://www.newyorker.com/magazine/2008/05/19/100-essential-jazz-albums
jazz_clips = [
    ["https://www.youtube.com/watch?v=vDqULFUg6CY", "davis"], #kind of blue
    ["https://www.youtube.com/watch?v=MiZp563Jnso", "armstrong"], #the very best of Louis a
    ["https://www.youtube.com/watch?v=1-JUy1qrKos", "ellington"], #ellington uptown
    ["https://www.youtube.com/watch?v=QXeEXnhuFzk", "fitzgerald"], #but not for me
    ["https://www.youtube.com/watch?v=yOKtvLqzhBg", "parker"], #the essential
    ["https://www.youtube.com/watch?v=gncbydxqE4Y", "holiday"], #lady in satin
    ["https://www.youtube.com/watch?v=v5eypUpQc7M", "evans"], #portrait in jazz complete
    ["https://www.youtube.com/watch?v=OXvS8ns9myY", "peterson"], #sound of the trio
    ["https://www.youtube.com/watch?v=B60tL9LdnbM", "lincoln"], #straight ahead
    ["https://www.youtube.com/watch?v=lBH-6CJYdJ4", "blakey"], #free for all
    ["https://www.youtube.com/watch?v=KJifh-S2Hw4", "tatum"], #tatum and ben webster
    ["https://www.youtube.com/watch?v=Ugxs64vQLbI", "carter"], #the best of betty carter
    ["https://www.youtube.com/watch?v=EAAfJ8mmVY4", "buddy_rich"], #the wailing buddy rich
    ["https://www.youtube.com/watch?v=D821Atw0HwQ", "adderley"], #portrait of
    ["https://www.youtube.com/watch?v=N_k0CF1VnNg", "beiderbecke"],
    ["https://www.youtube.com/watch?v=4qQVcjXopZo", "waller"],
    ["https://www.youtube.com/watch?v=WBAF1iGsGw0", "king_oliver"],
    ["https://www.youtube.com/watch?v=6ExvOmkmya4", "reinhardt"], #sultan of swing
    ["https://www.youtube.com/watch?v=L9kfPeTgOX4", "jelly_roll_morton"], # original recordings
    ["https://www.youtube.com/watch?v=ahxEN2GHUYA", "bechet"], # fabulous SB
    ["https://www.youtube.com/watch?v=xO2RWWqZqOc", "hawkins"], # nighthawk
    ["https://www.youtube.com/watch?v=qNrsOYF1qqw", "wilson_t"], # best piano recordings
    ["https://www.youtube.com/watch?v=coRFTtAco70", "young_l"], # oscar peterson trio
    ["https://www.youtube.com/watch?v=MyM-PlLWxco", "basie"], # complete atomic basie
    ["https://www.youtube.com/watch?v=xqTtM8Bv9vM", "goodman"], # best of BG
    ["https://www.youtube.com/watch?v=ir-1Fzdu7zE", "shavers_c"], #charlie shavers
    ["https://www.youtube.com/watch?v=Kze9ZLwAZuA", "chick_w"], # chick webb saga
    ["https://www.youtube.com/watch?v=NuaCviiAUSk", "carter_b"], #further definitions
    ["https://www.youtube.com/watch?v=iMOPcWSz9ro", "johnson_jp"], # fats walker
    ["https://www.youtube.com/watch?v=RUQsczC8wkk", "nat_king_cole_trio"], #after midnight
    ["https://www.youtube.com/watch?v=pden8LSWMkY", "dizzy_gillespie"], #
    ["https://www.youtube.com/watch?v=i61gSKmeQ74", "monk"], # solo monk
    ["https://www.youtube.com/watch?v=vJmSy-0mI_w", "marsh_w"], #live at hollywood
    ["https://www.youtube.com/watch?v=7mbsSQPQsPc", "powell_b"], #the scene changes
    ["https://www.youtube.com/watch?v=q9Cgj9NH-kY", "mulligan_g"], #quartet
    ["https://www.youtube.com/watch?v=5MwwS8ZAbr8", "brown_n_roach"], 
    ["https://www.youtube.com/watch?v=fVsSIVL2qog", "vaughan_s"], 
    ["https://www.youtube.com/watch?v=kqOJ6UI6_3w", "mingus"], # FIRST FEW SECS A BIT CLASSICAL-LY
    ["https://www.youtube.com/watch?v=PI7Jsasfp54", "rollins_s"], # out west
    ["https://www.youtube.com/watch?v=xM_GrwYQUtg", "puente"], # best of
    ["https://www.youtube.com/watch?v=s3xjnM64g-A", "sun_ra"], 
    ["https://www.youtube.com/watch?v=RAena9F9oSE", "jamal_a"], # session 1971
    ["https://www.youtube.com/watch?v=Vc1BDi1XN2Q", "brubeck_d"], # the essential
    ["https://www.youtube.com/watch?v=RyRTQKljxIM", "witherspoon_j"], #live at the mint
    ["https://www.youtube.com/watch?v=ua5S8UmoeWs", "ornette_c"], # body meta
    ["https://www.youtube.com/watch?v=p7uVPze7c3o", "hubbard"], #open sesame
    ["https://www.youtube.com/watch?v=U1mQzxx3zMI", "smith_j"], # salle pleyel
    ["https://www.youtube.com/watch?v=hD97alvMF9s", "washington_d"], # greatest hits
    ["https://www.youtube.com/watch?v=VBBWqbPaJgs", "coltrane"], #blue train
    ["https://www.youtube.com/watch?v=zRekHkcS2X0", "dolphy_e"], # out to lunch
    ["https://www.youtube.com/watch?v=poz_xCQMRSU", "mclean_j"], # a fickle sonance
    ["https://www.youtube.com/watch?v=hyaTChd-7BY", "getz_s"], # sg at large
    ["https://www.youtube.com/watch?v=X9npugsswT0", "gordon_d"], # the complete blue note
    ["https://www.youtube.com/watch?v=tPkyAs3na1Q", "hill_a"], # point of departure
    ["https://www.youtube.com/watch?v=z59xUDv15hw", "morgan_l"], # sonic boom
    ["https://www.youtube.com/watch?v=xWsIG5sNq1Q", "ayler_a"], # spiritual unity
    ["https://www.youtube.com/watch?v=ZTYDEcp-a5Y", "shepp_a"],
    ["https://www.youtube.com/watch?v=nW810DEscVI", "silver_h"], #six pieces of silver
    ["https://www.youtube.com/watch?v=IFBeo0cGu7c", "montgomery_w"], #very best of
    ["https://www.youtube.com/watch?v=5yJWcxzZBVE", "taylor_c"], #conquistador
    ["https://www.youtube.com/watch?v=FghBZ7mL4c4", "sinatra_f"], # greatest hits
    ["https://www.youtube.com/watch?v=KRLwsSbqlwo", "chick_c"], # APPLAUSE AT BEGINNING
    ["https://www.youtube.com/watch?v=bZhTwoO0Fd8", "jarrett"], # the Koln concert
    ["https://www.youtube.com/watch?v=cg9PDNuQiLk", "world_saxaphone_quartet"], 
    ["https://www.youtube.com/watch?v=unRwO30PtgM", "jones"], # trio recordings
    ["https://www.youtube.com/watch?v=B6DGPZngY7g", "wilson_c"], #belly of the sun
    ["https://www.youtube.com/watch?v=jS9dscuKsGA", "marsalis_w"], # APPLAUSE AT BEGINNING
    ["https://www.youtube.com/watch?v=w5ETUKz5RGM", "charlap_bill"], # written in the stars
]

def init_directories(old_path=BASE_PATH):
    if not old_path.endswith("/"):
        old_path += "/"
    os.makedirs(old_path + "dataset/")
    os.makedirs(old_path + "dataset/Classical")
    os.makedirs(old_path + "dataset/Jazz")

def download_and_split(path, n_clips_per_link, list_of_clips):
    for clip in list_of_clips:
        try:
            download(clip, path)
            split_mp4_into_wavs(path + clip[1], n_clips_per_link)
            print("Loaded " + clip[1])
        except Exception as err:
            print("Exception encountered loading " + clip[1])
            print(err)
            continue
        
def download(clip, path):
    audio_stream = YouTube(clip[0]).streams.filter(file_extension="mp4")
    audio_stream.first().download(output_path=path, filename=clip[1] + ".mp4")

def split_mp4_into_wavs(path, n_clips, length=LENGTH_OF_CLIP):
    filename = path.split('/')[-1]
    # Insert Local Video File Path
    clip = mp.VideoFileClip(path + ".mp4")

    # Insert Local Audio File Path
    
    clip.audio.write_audiofile("output.wav",codec='pcm_s16le')
    clip.close()
    
    sound = AudioSegment.from_file("output.wav", format="wav", channels=1)
        
    j = 0
    for i in range(n_clips):
        j += len(sound) // n_clips
        chunk = sound[j:(j + 5000)]
        with open(path+"-%s.wav" % i, "wb") as f:
            chunk.export(f, format="wav")
    try:
        os.remove(path + ".mp4")
    except:
        print(filename + ".mp4 could not be removed")

init_directories()

# Load classical clips
path = BASE_PATH + "/dataset/Classical/"
n_clips_per_link = int(NUMBER_OF_CLIPS / 2 / len(classical_clips))
download_and_split(path, n_clips_per_link, classical_clips)

# Load jazz clips
path = BASE_PATH + "/dataset/Jazz/"
n_clips_per_link = int(NUMBER_OF_CLIPS / 2 / len(jazz_clips))
download_and_split(path, n_clips_per_link, jazz_clips)

os.remove("output.wav")
