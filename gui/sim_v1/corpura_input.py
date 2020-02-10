import os

corpura_dict = {
#                r'corpus_1': {r'search_dir': r'C:\Users\erdig\Desktop\SURGE',
#                             r'doc': True,
#                             r'docx': True,
#                             r'pdf': False,
#                             r'txt': False,
#                             r'language': r'norwegian'
#                                     },
                # r'corpus_2': {r'search_dir': r'C:\Users\erdig\Desktop\Tilbud',
                #                             r'doc': True,
                #                             r'docx': True,
                #                             r'pdf': False,
                #                             r'txt': False,
                #                             r'language': r'norwegian'
                #                                     },
                # r'corpus_3': {r'search_dir': r'C:\Users\erdig\Desktop\N800 - utvalg',
                #                             r'doc': False,
                #                             r'docx': True,
                #                             r'pdf': False,
                #                             r'txt': False,
                #                             r'language': r'norwegian'
                #                                     },
                r'corpus_4': {r'search_dir': r'C:\Users\erdig\Desktop\CV (2020-01-17)',
                                            r'doc': False,
                                            r'docx': True,
                                            r'pdf': False,
                                            r'txt': False,
                                            r'language': r'norwegian'
                                                    },
                # r'corpus_5': {r'search_dir': r'J:\50_Energi\540_Maskin\6_Tilbud',
                #                             r'doc': False,
                #                             r'docx': True,
                #                             r'pdf': False,
                #                             r'txt': False,
                #                             r'language': r'norwegian'
                #                                     },
                }

corpura_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura')
#corpura_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura'
corpura_dict_dir =os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','corpura','corpura_dict.p')
#corpura_dict_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\corpura\corpura_dict.p'
