formats = {
    'image/':['gif', 'jpg', 'jpeg', 'png'],
    'application/':['zip', 'pdf'],
    'text/plain':'txt'
}

media = input('Media file name? ').lower().strip().split('.')
if len(media) > 1:
    if 'jpg' in media:
        media = [media[0], 'jpeg']
    if media[-1] in formats['image/']:
        print(list(formats.keys())[0] + media[-1])

    elif media[-1] in formats['application/']:
        print(list(formats.keys())[1] + media[-1])

    elif media[-1] == formats['text/plain']:
        print(list(formats.keys())[-1])

    else:
        print('application/octet-stream')
else:
    print('application/octet-stream')