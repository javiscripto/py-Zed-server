import os
from livereload import Server


def watch_directories(server, root='.'):
    for subdir, dirs, files in os.walk(root):
        for dir_name in dirs:
            
            server.watch(os.path.join(subdir, dir_name, '*.html'))
            server.watch(os.path.join(subdir, dir_name, '*.css'))
            server.watch(os.path.join(subdir, dir_name, '*.js'))
            server.watch(os.path.join(subdir, dir_name, '*.jsx'))
            server.watch(os.path.join(subdir, dir_name, '*.ts'))
            server.watch(os.path.join(subdir, dir_name, '*.tsx'))
            server.watch(os.path.join(subdir, dir_name, '*.png'))
            server.watch(os.path.join(subdir, dir_name, '*.jpg'))
            server.watch(os.path.join(subdir, dir_name, '*.svg'))

server = Server()



watch_directories(server)

server.watch('index.html')


image_extensions = ['jpg', 'png', 'webp', 'gif', 'svg', 'mp4', 'mov']

for ext in image_extensions:
    server.watch(f'assets/*.{ext}')

server.serve(root='.', host='0.0.0.0', port=3000)
