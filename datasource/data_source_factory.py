class DataSourceFactory:
    def __init__(self, data_source):
        self.data_source = data_source

    def create():
        if (self.data_source.type == 'html'):
            obj = HtmlDataSource(self.data_source)
        return obj

