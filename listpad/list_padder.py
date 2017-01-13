class ListPadder:

    def __init__(self, lengths, bottom_dummy, centerize):
        assert all(isinstance(hier, int) and hier >
                   0 for hier in lengths.keys())

        self._lengths = lengths  # hier -> length
        self._dummies = {0: bottom_dummy}  # hier -> dummy
        self._centerize = centerize

    def _dummy(self, hier):
        if hier in self._dummies:
            return self._dummies[hier]

        assert hier != 0
        self._dummies[hier] = [self._dummy(hier - 1)] * self._lengths[hier]
        return self._dummies[hier]

    def pad(self, list_):
        if not isinstance(list_, list):
            return list_

        padded_sub_lists = [self.pad(sub_list) for sub_list in list_]

        hier = self._hier(list_)
        length = self._lengths[hier]

        if length is None:
            return padded_sub_lists

        return self._pad_list_of_padded_sub_lists(padded_sub_lists)

    def _pad_list_of_padded_sub_lists(self, list_):
        hier = self._hier(list_)
        length = self._lengths[hier]
        dummy_head, dummy_tail \
            = self._split_in_half(self._dummy(hier)[:max(length - len(list_), 0)])
        return dummy_head + list_[:length] + dummy_tail \
            if self._centerize else \
            list_[:length] + dummy_head + dummy_tail

    def _hier(self, list_):
        if not isinstance(list_, list):
            return 0

        assert all(self._hier(elem) == self._hier(list_[0]) for elem in list_)
        assert len(list_) > 0
        return self._hier(list_[0]) + 1

    @staticmethod
    def _split_in_half(list_):
        half_length = len(list_) // 2
        return list_[:half_length], list_[half_length:]
