import os

corpura_dict = {r'corpus_1': {r'search_dir': r'/Users/Erik/Dropbox',
                            r'doc': True,
                            r'docx': True,
                            r'pdf': False,
                            r'txt': False,
                            r'language': r'english'
                            },
                # 'corpus_2': {'search_dir': '/Users/Erik/Documents/Jobb',
                #             'docx': True,
                #             'pdf': True,
                #             'txt': False,
                #             'language': 'norwegian'
                #             },
                }

corpura_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura')
#corpura_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura'
corpura_dict_dir =os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura','corpura_dict.p')
#corpura_dict_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura\corpura_dict.p'
