import requests
import moviepy.editor as mp
import os.path

def hash(str):
  # 'p' and 'm' some positive integers whose choice affects on performance and security of the hash function
  p = 111
  m = 10**9 + 223

  result = 0
  for i in range(len(str)):
    result += ord(str[i]) * p**i % m

  return result


def convert_to_gif(link):
  if not os.path.exists('from_TickTock'): # Create folder 'from_TickTock' if not exist
    os.mkdir('from_TickTock')

  # Create unique filename (video_1, video_2, video_3... etc.)
  filepath = 'from_TickTock/video_1.gif'
  while(os.path.exists(filepath)):
    video_num = int(filepath[20:-4]) + 1
    filepath = 'from_TickTock/video_' + str(video_num) + '.gif'

  r = requests.get(link, stream = True) # Get video by link
  with open('temp.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024*1024):
      if chunk:
        f.write(chunk)

  convert_to_gif = mp.VideoFileClip('temp.mp4')
  convert_to_gif.write_gif(filepath) # Write file in gif format


# Execute task 1
s = 'Python Bootcamp'
print(hash(s))

# Execute task 2
convert_to_gif('https://v16-webapp.tiktok.com/bbdb7f7f47041f7644863f0525cbff50/62e89345/video/tos/useast2a/tos-useast2a-pve-0068/d14881bf45d54f44a135192891d5ce45/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2074&bt=1037&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZOi3Kwe2Nk8Jyl7Gb&mime_type=video_mp4&qs=0&rc=NzdoNzs5aTk6ODs3NzdlOkBpajNvaDQ6ZjNzZTMzNzczM0AyYmNhMjExXjMxYTIxNS0yYSNhYm1ycjRfLWRgLS1kMTZzcw%3D%3D&l=20220801210009010190219228116593DF')
