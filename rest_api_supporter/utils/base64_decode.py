import base64
import io
from PIL import Image

'''
def base64_decode(full_encoded):
    if isinstance(full_encoded, str) and "base64," in full_encoded:
        #print(full_encoded) #data:image/png;base64,/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
                             #data:audio/wav;base64,UklGRiTuAgBXQVZFZm...At84WACNZGwA=
        front = full_encoded.split('base64,')[0]
        base64_encoded = full_encoded.split('base64,')[1]
        base64_decoded = base64.b64decode(base64_encoded)
        if "image" in front: #이미지
            image = Image.open(io.BytesIO(base64_decoded))
            return image
        elif "audio" in front: #오디오
            return base64_decoded
    else:
        #print(full_encoded) #/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
                             #UklGRiTuAgBXQVZFZm...At84WACNZGwA=
        base64_decoded = base64.b64decode(full_encoded)
        image = Image.open(io.BytesIO(base64_decoded))
        return image
'''
def base64_decode(full_encoded):
    if isinstance(full_encoded, str) and "base64," in full_encoded:
        #print(full_encoded) #data:image/png;base64,/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
                             #data:audio/wav;base64,UklGRiTuAgBXQVZFZm...At84WACNZGwA=
        front = full_encoded.split('base64,')[0]
        base64_encoded = full_encoded.split('base64,')[1]
        base64_decoded = base64.b64decode(base64_encoded)
        if "image" in front: #이미지
            image = Image.open(io.BytesIO(base64_decoded))
            return image
        elif "audio" in front: #오디오
            #return base64_decoded #bytes
            file = "audio.wav"
            with open(file, "wb") as f:
                f.write(base64_decoded) #bytes
            base64_decoded, samplerate = sf.read(file) #numpy array
            return base64_decoded
    else:
        #print(full_encoded) #/9j/4AAQSkZJRgABAQ...2qjR37P/2Q==
                             #UklGRiTuAgBXQVZFZm...At84WACNZGwA=
        base64_decoded = base64.b64decode(full_encoded)
        image = Image.open(io.BytesIO(base64_decoded))
        return image
