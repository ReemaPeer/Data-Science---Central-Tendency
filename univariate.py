class univariate():
        def Qualquan (dataset):
            Qual = []
            Quan = []
            for col in dataset.columns:
                if dataset[col].dtype == 'O':
                    Qual.append(col)
                else:
                    Quan.append(col)
            return Qual, Quan      