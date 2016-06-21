import unittest
import glob
from find_reg_ex import find

class PatternFinderTest(unittest.TestCase):
	def setUp(self):
		self.files = glob.glob('input/*.html')

	def test_escaped_characters(self):
		pattern = 'class="hs-featured-image-link">\\\\n'
		ids = find(pattern, self.files)
		self.assertEqual(len(ids), 184)
		self.assertCountEqual(ids, ['8689777951', '8689784181', '8689782501', '8735757831', '8689817761', '8689771651', '8689867571', '8830391361', '8887672971', '9131534371', '8938797101', '9792103001', '9792112911', '9792118181', '9792106691', '9792117671', '9792117991', '9792163411', '9792142821', '9792164011', '9792170381', '8689778768', '8689876738', '8718637628', '8689784058', '8718668088', '8689814798', '8807903968', '9577982058', '9515954888', '9768517678', '9792105378', '9792107988', '9792108908', '9792110258', '9792110838', '9792117318', '9792121078', '9792145548', '9792147428', '9792130368', '9792162808', '9792166908', '8689782960', '8718639810', '8718634670', '8689802720', '8718701550', '8726431680', '8689825430', '8689776840', '8689782350', '8703002370', '8718734740', '8689771490', '8689782000', '8966537150', '8774696770', '8801126980', '8914265880', '9792097420', '9792101810', '9792111030', '9792110600', '9792115560', '9792135280', '9792125940', '9792166280', '9792166720', '9792167810', '9792169720', '8718634193', '8689840663', '8718698473', '9578049003', '9462848903', '9792104743', '9792108533', '9792114713', '9792115413', '9792117843', '9792123523', '9792126383', '9792146803', '9792146943', '9792163703', '8689803959', '8718637159', '8689857589', '8689775959', '8718734909', '8718710029', '8689777239', '9792106329', '9419490539', '9792104959', '9792108399', '9792103369', '9792112099', '9792123389', '9792137009', '9792167659', '9792163249', '9792164229', '9792165739', '8689783115', '8689761255', '8689782735', '8726432355', '8689782215', '8689779075', '8689776375', '8689782615', '8689777615', '9620941865', '9131919555', '9792108685', '9792115115', '9792145415', '9792136095', '9792167475', '9792170165', '8718668756', '8689814276', '8718634406', '8718735246', '9150898406', '9462820686', '9792119496', '9792102826', '9792121906', '9792167086', '9792170566', '8718636987', '8689777077', '8718730147', '8729874757', '9792116937', '9792119167', '9792122557', '9792131747', '9792167287', '9792169917', '9792170787', '8689781882', '8718639972', '8718729442', '8689881672', '8689837712', '8718734392', '8801176372', '8857919752', '9792097882', '9792099822', '9792108192', '9792089872', '9792117142', '9792117442', '9792118792', '9792163002', '9792163112', '9792162582', '8702980224', '8718659914', '8718647134', '8718690354', '8689778444', '8689777474', '8689782104', '8689814904', '8718633994', '8902100194', '8830442834', '8957770184', '9792105144', '9792112744', '9792118604', '9792107014', '9792166144', '9792129844', '9792163554', '9792139394', '9792165954', '9792166474'])
	
	def test_find_regex_with_numbers(self):
		pattern = 'Section \d+ Refresh'
		ids = find(pattern, self.files)
		self.assertEqual(len(ids), 2)
		self.assertCountEqual(ids, ['9028094287','9780103281'])
	
if __name__ == "__main__":
	unittest.main()