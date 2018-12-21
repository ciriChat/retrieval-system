# from unittest import TestCase, main
# from unittest.mock import patch
#
# from main import SubtitleService
#
#
# class TestSubtitleService(TestCase):
#     def setUp(self):
#         self.service = SubtitleService()
#
#     @patch('aaaa.main.subtitle.model.SubtitleRepository.find_by_hash3')
#     def test_get(self, find_by_hash3):
#         mock = find_by_hash3.return_value = 'asd'
#
#         res = self.service.get_subtitle('xdd')
#
#         self.assertEqual('asd', res)
#
#
# if __name__ == '__main__':
#     main()
