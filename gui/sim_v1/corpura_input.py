import os

corpura_dict = {r'corpus_1': {r'search_dir': r'C:\Users\erdig\Desktop\Vannveisutstyr\Rør',
                            r'doc': True,
                            r'docx': True,
                            r'pdf': False,
                            r'txt': False,
                            r'language': r'english'
                            },
                r'corpus_2': {r'search_dir': r'C:\Users\erdig\Desktop\Vannveisutstyr\Rør\Stål-jernrør',
                            r'doc': True,
                            r'docx': True,
                            r'pdf': False,
                            r'txt': False,
                            r'language': r'english'
                                    },
                }

corpura_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura')
#corpura_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura'
corpura_dict_dir =os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura','corpura_dict.p')
#corpura_dict_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura\corpura_dict.p'
