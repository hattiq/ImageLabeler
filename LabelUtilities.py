from abc import ABC, abstractmethod


class LabelMaker:
    def __init__(self, names: [str]):
        self.__names = names
        self.__labels = {}

        for name in self.__names:
            self.__labels[name] = False

    def toggle(self, name: str):
        self.__labels[name] = not self.__labels[name]

    @property
    def label(self) -> dict:
        return self.__labels.copy()


class LabelFormatterInterface(ABC):
    @abstractmethod
    def getFormattedLabel(self, label: dict) -> str:
        pass


class ListPositionalLabelFormatter(LabelFormatterInterface):
    def __init__(self, positionedNames: [str]):
        self.__positionedNames = positionedNames

    def getFormattedLabel(self, label: dict) -> str:
        formattedLabel = []

        for name in self.__positionedNames:
            formattedLabel.append(1 if label[name] else 0)

        return str(formattedLabel)
