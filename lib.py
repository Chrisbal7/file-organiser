extensions = {
    'audio': ['aa', 'aac', 'aax', 'act', 'aiff', 'alac', 'amr',
              'ape', 'au', 'awb', 'dss', 'dvf', 'flac', 'gsm',
              'iklax', 'ivs', 'm4a', 'm4b', 'm4p', 'mmf', 'mp3',
              'mpc', 'msv', 'nmf', 'ogg', 'oga', 'mogg', 'opus',
              'ra', 'rm', 'raw', 'rf64', 'sln', 'tta', 'voc',
              'vox', 'wav', 'wma', 'wv', 'webm', '8svx', 'cda'],

    'video': ['webm', 'mkv', 'flv', 'ogv', 'ogg', 'drc', 'gifv',
              'mng', 'avi', 'mts', 'm2ts', 'ts', 'mov', 'qt',
              'wmv', 'yuv', 'rm', 'rmvb', 'viv', 'asf', 'amv',
              'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe',
              'mpv', 'm2v', 'svi', '3gp', '3g2', 'mxf', 'roq',
              'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b'],

    'image': ['jpeg', 'jpg', 'gif', 'png', 'webp', 'jp2', 'hdr',
              'heif', 'avif', 'jxl', 'tiff', 'bmp', 'ppm', 'pgm',
              'pbm', 'pnm', 'svg'],

    'document': ['docx', 'xlsx', 'doc', 'djvu', 'doc',
                 'html', 'htm', 'fb2', 'md', 'odt', 'sxw', 'oxps',
                 'pdf', 'ps', 'rtf', 'svg', 'wpd', 'wp', 'wp7',
                 'ppt', 'pptx', 'xls', 'epub'],

    'archive': ['a', 'ar', 'cpio', 'shar', 'lbr', 'iso', 'mar',
                'sbx', 'tar', 'br', 'bz2', 'f', 'xf', 'genozip',
                'gz', 'lz', 'lz4', 'lzma', 'lzo', 'rz', 'sfark',
                'sz', 'q', 'z', 'xz', 'zst', '7z', 's7z', 'ace',
                'afa', 'alz', 'apk', 'arc', 'ark', 'cdx', 'arj',
                'b1', 'b6z', 'ba', 'bh', 'cab', 'car', 'cfs',
                'cpt', 'dar', 'dd', 'dgc', 'dmg', 'ear', 'gca',
                'ha', 'hki', 'ice', 'jar', 'kgb', 'lzh', 'lha',
                'lzx', 'pak', 'partimg', 'paq6', 'paq7', 'paq8',
                'pea', 'phar', 'pim', 'pit', 'qda', 'rar', 'rk',
                'sda', 'sea', 'sen', 'sfx', 'shk', 'sit', 'sitx',
                'sqx', 'tar.gz', 'tgz', 'tar.z', 'tar.bz2', 'tbz2',
                'tar.lz', 'tlz', 'tar.xz', 'txz', 'tar.zst', 'uc',
                'uc0', 'uc2', 'ucn', 'ur2', 'ue2', 'uca', 'uha',
                'war', 'wim', 'xar', 'xp3', 'yz1', 'zip', 'zipx',
                'zoo', 'zpaq', 'zz', 'ecc', 'ecsbx', 'par', 'par2',
                'rev'],

    'package': ['deb', 'pkg', 'mpkg', 'rpm', 'tgz', 'msi', 'jar',
                'crx', 'pkg.tar.zst', 'pkg.tar', 'apk', 'exe'],

    'library': ['dll']
}

media_formats = extensions['audio']

reserved_dirs = {'windows': ['system32', 'Program Files (x86)',
                             'windows', 'Program Files', 'PerfLogs',
                             'MSOCache', 'ProgramData', 'Recovery',
                             '$Recycle.Bin', 'System Volume Information',
                             '$WinREAgent'],
                 'linux': ['bin', 'boot', 'cdrom', 'dev', 'etc',
                           'lib', 'lib32', 'lib64', 'libx32',
                           'mnt', 'opt', 'proc', 'root', 'run',
                           'sbin', 'snap', 'srv', 'sys', 'tmp',
                           'usr', 'var'],
                 'darwin': ['Applications', 'Library', 'Network',
                            'System', 'bin', 'cores', 'dev', 'etc@',
                            'net', 'private', 'sbin', 'tmp@', 'usr',
                            'var@']
                 }

tanzania_artists = ['Diamond Platnumz', 'Ali kiba', 'Nahreel', 'Mbosso',
                    'vanessa Mdee', 'ben Pol', 'Cool James', 'AY',
                    'ray c', 'barnaba classic', 'x plastaz', 'nedy music',
                    'jay mitta', 'shilole', 'lavalava', 'baby madaha', 'harmonize',
                    'rayvanny', 'nandy', 'lady jaydee', 'dogo janja', 'remmy ongala',
                    'navy kenzo', 'rich mavoko', 'hamisa mobetto', 'kusah', 'msafiri zawose',
                    'lava lava', 'siti muharam', 'tommy flavour', 'saida karoli', 'rapcha',
                    'zuchu', 'jux', 'bill nass', 'marioo', 'dully sykes', 'shetta',
                    'juma nature', 'aslay', 'darassa', 'platform tz', 'turunesh',
                    'professor jay', 'queen darleen', 'jay melody', 'dulla makabila',
                    'abby chams']
