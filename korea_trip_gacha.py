import random
import json


class KoreanDistrictGacha:
    def __init__(self):
        self.data = self.load_data()
        self.city, self.dist = self.eodiro_galkkayo()

    def load_data(self):
        with open("./korean_district_data.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def eodiro_galkkayo(self):
        district = self.data[random.randint(0, len(self.data) - 1)]
        city = list(district.keys())[0]
        districts = district[city]
        selected_district = districts[random.randint(0, len(districts) - 1)]
        print("여행지 랜덤뽑기 결과는!!!")
        print(f"{city} {selected_district}로 가시면 되겠습니다~~🥳🥳")
        return city, selected_district


if __name__ == "__main__":
    gacha = KoreanDistrictGacha()
