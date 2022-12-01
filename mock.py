class MockGoogleAdsData:
    class MockGoogleAdsDate:
        def __init__(self, i):
            if type(i) is dict:
                for key in i:
                    if type(i[key]) is dict:
                        print("setting attribute: ", key, i[key])
                        setattr(self, key, self.__class__(i[key]))
                    else:
                        print("setting attribute: ", key, i[key])
                        setattr(self, key, i[key])

        def __getattr__(self, item):
            if not self.__dict__.get(item):
                return None
            else:
                return getattr(self, item)

    batch = 0

    def __init__(self, data):
        self.results = []
        for i in data:
            self.results.append(self.MockGoogleAdsDate(i))

    def __iter__(self):
        return self

    def __next__(self):
        self.batch += 1
        if self.batch > 1:
            raise StopIteration
        return self
