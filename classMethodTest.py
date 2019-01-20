# -*- coding: utf-8 -*-
class Boku(object):
    # これはクラス変数
    subject = "ぼくは"
    name = "ドラえもん"
    

    def __init__(self, nickname):
        self.nickname = nickname # これはインスタンス変数
    


    # これはインスタンスメソッド
    def get_name_instance(self, class_var=False):
        if class_var:
            return Boku.subject + Boku.name + "。"
        else:
            return "ぼくは" + self.nickname + "。"

    def set_name_instance(self, nickname, class_var=False):
        if class_var:
            Boku.name = nickname
        else:
            self.nickname = nickname

    def dialogue_instance(self, dialogue, class_var=False):
        return self.get_name_instance(class_var) + dialogue + "！"
    



    # これはクラスメソッド
    @classmethod
    def get_name_class(cls):
        return cls.subject + cls.name + "。"

    @classmethod
    def set_name_class(cls, nickname):
        cls.name = nickname

    @classmethod
    def dialogue_class(cls, dialogue):
        return cls.get_name_class() + dialogue + "！"
    



    # これはスタティックメソッド
    @staticmethod
    def get_name_static():
        return "ぼくは" + Boku.name + "。"

    @staticmethod
    def set_name_static(nickname):
        Boku.name = nickname

    @staticmethod
    def dialogue_static(dialogue):
        return get_name_static() + dialogue + "！"



class Ore(Boku):
    subject = "オレは"