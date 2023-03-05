def main():
    s = input("File name: ")
    print(mime_type(s))

def mime_type(s):
    s1 = s.rpartition('.')[2]
    match s1:
        case 'gif':
            return 'image/gif'
        case 'jpg':
            return 'image/jpeg'
        case 'jpeg':
            return 'image/jpeg'
        case 'png':
            return 'image/png'
        case 'pdf':
            return 'application/pdf'
        case 'txt':
            return 'text/plain'
        case 'zip':
            return 'application/zip'
        case _:
            return 'application/ocet-stream'


main()