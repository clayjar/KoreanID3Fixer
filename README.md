# KoreanID3Fixer #

KoreanID3Fixer is a Python program to fix the Korean encoding issue for ID3 attributes for MP3 files. This provides an easy-to-use solution for updating the metadata of songs in a folder.

KoreanID3Fixer는 MP3 파일의 ID3 속성에 대한 한국어 인코딩 문제를 해결하는 Python 프로그램입니다. 폴더에 있는 노래의 메타데이터를 업데이트하기 위한 사용하기 쉬운 솔루션으로 제공합니다.

## Features (특징) ##

- Automatic detection of incorrect Korean encoding in ID3 tags
- Conversion of incorrectly encoded ID3 tags to properly encoded Unicode
- Support for batch processing of music files
- Compatible with both ID3v1 and ID3v2 tags

- ID3 태그의 잘못된 한글 인코딩 자동 감지
- 잘못 인코딩된 ID3 태그를 올바르게 인코딩된 유니코드로 변환
- 음악 파일 일괄 처리 지원
- ID3v1 및 ID3v2 태그 모두와 호환 가능

## Installation (설치) ##

This assumes you already have Python 3 installed. Python 3이 이미 설치되어 있는 것을 가정합니다.

(This is tested on Ubuntu 22.04. Ubuntu 22.04에서 확인되었습니다.):

You have installed the mutagen library first.
mutagen 라이브러리를 먼저 설치해야합니다.

```bash
$ apt update && apt install -y python3-mutagen
```

Note: the previous package maintainer had an example with easy_install, which was deprecated many years ago. 
참고: 이전 패키지 관리자는 몇 년 전에 더 이상 사용되지 않는 easy_install에 대한 예제를 가지고 있었습니다.

Once you have `mutagen` installed, you can either copy the fix_kr_id3.py file to a place where it's accessible (e.g. ~/bin) or clone the repository.
`mutagen`이 설치되면 fix_kr_id3.py 파일을 액세스 가능한 위치(예: ~/bin)에 복사하거나 GitHub에서 소스 저장소를 복제할 수 있습니다.

## Usage (사용)

If you run the script it will update the mp3 files in the current folder.
원하시는 디렉토리에서 실행하면 현재 디렉토리에 있는 mp3 파일을 업데이트합니다.

Say you have files like this 이렇게 깨진 한글이 있다면:
![Before applying the fix](https://private.michaelhan.net/img/id3fix-before.png "Before the fix")

```bash
$ cd ~/music

$ python ~/bin/fix_kr_id3.py

checking /mnt/e/tray5/Downloads/music/010. 싸이-04-DADDY (Feat. CL of 2NE1).mp3
The string contains characters that are not suppoddkkrted in 'iso-8859-9' encoding.
  album = 칠집싸이다
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
updating /mnt/e/tray5/Downloads/music/010. 싸이-04-DADDY (Feat. CL of 2NE1).mp3
checking /mnt/e/tray5/Downloads/music/018. 싸이-03-나팔바지.mp3
The string contains characters that are not supported in 'iso-8859-9' encoding.
  album = 칠집싸이다
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
updating /mnt/e/tray5/Downloads/music/018. 싸이-03-나팔바지.mp3
checking /mnt/e/tray5/Downloads/music/025. 디셈버-01-네게 줄 수 있는건 오직 사랑뿐.mp3
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
The string contains characters that are not supported in 'iso-8859-9' encoding.
The string contains characters that are not supported in 'iso-8859-1' encoding.
The string contains characters that are not supported in 'iso-8859-9' encoding.
  artist = 디셈버
The string contains characters that are not supported in 'iso-8859-9' encoding.
  albumartist = 디셈버
updating /mnt/e/tray5/Downloads/music/025. 디셈버-01-네게 줄 수 있는건 오직 사랑뿐.mp3
```

After the fix has been applied, it should look like this.  고쳐진 후에 이렇게 한글이 바르게 보입니다.
![After applying the fix](https://private.michaelhan.net/img/id3fix-after.png "After the fix")

If you still see garbled Korean characters, please add other encodings and try again.
만약 맞는 encoding 를 찾지 못해 계속 한글이 깨져있다면 파일 안에서 추가로 다른 encoding 을 추가한 후 다시 해보세요.

```python
    source = ['iso-8859-9','iso-8859-1','cp949']
```

## Contribution (돕는 방법) ##

The main part of the code was originally forked from an old repository *[here](https://github.com/mix1009/fix_id3_kr_encoding)*. Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
코드의 주요 부분은 원래 *[박천구](https://github.com/mix1009/fix_id3_kr_encoding)*님의 repo에서 포크되었습니다. 기여는 오픈 소스 커뮤니티를 배우고, 영감을 주고, 창조할 수 있는 놀라운 장소로 만드는 것입니다. 귀하의 기여에 크게 감사드립니다.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License ##

Distributed under the MIT License. See 'LICENSE' for more information.

## Contact ##

Michael Han <clayjar@gmail.com>

Project Link: (https://github.com/clayjar/KoreanID3Fixer)

Original project link: (https://github.com/mix1009/fix_id3_kr_encoding)
