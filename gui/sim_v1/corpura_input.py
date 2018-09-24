import os

corpura_dict = {r'corpus_1': {r'search_dir': r'C:\Users\erdig\Desktop\6_Tilbud\Vannkraft\2017',
                            r'doc': True,
                            r'docx': True,
                            r'pdf': False,
                            r'txt': False,
                            r'language': r'norwegian'
                            },
                r'corpus_2': {r'search_dir': r'C:\Users\erdig\Desktop\6_Tilbud\Vannkraft\2018',
                            r'doc': True,
                            r'docx': True,
                            r'pdf': False,
                            r'txt': False,
                            r'language': r'norwegian'
                                    },
                }

corpura_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura')
#corpura_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura'
corpura_dict_dir =os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura','corpura_dict.p')
#corpura_dict_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura\corpura_dict.p'
