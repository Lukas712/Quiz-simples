from abc import abstractmethod, ABC
from typing import Type

class Perguntas(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        self.__numero_questoes = None
        self.__questao_correta = None
    
    @abstractmethod
    def questão(self) -> None:
        pass

    @abstractmethod
    def alternativas(self) -> None:
        pass

    @abstractmethod
    def resposta(self) -> None:
        pass

    @abstractmethod
    def verifica_resposta(self, alternativa_selecionada: str) -> bool:
        pass

    @abstractmethod
    def verifica_alternativa(self, alternativa: str) -> bool:
        pass

    @abstractmethod
    def errou(self) -> None:
        pass

    @abstractmethod
    def acertou(self) -> None:
        pass

class Questão1(Perguntas):

    def __init__(self) -> None:
        self.__numero_questoes = 0
        self.__questao_correta = "B"
    
    def questão(self) -> None:
        print("Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?")
        self.alternativas()
        self.resposta()

    def alternativas(self) -> None:
        questões = {"A": "Tem entre 2 a 4 litros. São retirados 450 mililitros", "B": "Tem entre 4 a 6 litros. São retirados 450 mililitros", "C": "Tem 10 litros. São retirados 2 litros", "D": "Tem 7 litros. São retirados 1,5 litros", "C": "Tem 0,5 litros. São retirados 0,5 litros"}
        for options in questões:
            print(f"{options} - {questões[options]}")
        self.__numero_questoes = len(questões)

    def verifica_alternativa(self, alternativa: str) -> bool:
        return type(alternativa) == str and chr(65 + self.__numero_questoes) >= alternativa.upper() >= "A"
    
    def resposta(self) -> None:
        alternativa = input("Digite a sua resposta: ")
        while not self.verifica_alternativa(alternativa):
            alternativa = input("Erro, escolha dentro das opções: ")
        if self.verifica_resposta(alternativa.upper()):
            self.acertou()
        else:
            self.errou()
            
    def acertou(self) -> None:
        print("Você acertou!")

    def errou(self) -> None:
        print(f"Você errou, a resposta correta era {self.__questao_correta}")

    def verifica_resposta(self, alternativa_selecionada: str) -> bool:
        return alternativa_selecionada == self.__questao_correta
        
class Quiz:

    def start_quiz(self, question: Type[Perguntas]) -> None:
        question.questão()

questao = Questão1()
quiz = Quiz()
quiz.start_quiz(questao)

