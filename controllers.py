from flask import request
from ntscraper import Nitter


class Controller:
    def get_nitter(self):
        try:
            scraper = Nitter(log_level=1, skip_instance_check=False)

            request_data = request.get_json()
            cari    = request_data['cari']
            limit   = request_data['limit']
            jenis   = request_data['jenis']

            result_tweets = scraper.get_tweets(cari, mode=jenis, number=limit)
            total_data = len(result_tweets['tweets'])
    
            response_data = {
                'status_code'   : 1,  # Success
                'total_data'    : total_data,
                'msg'           : "success",
                'data'          : result_tweets['tweets']
            }
    
            return response_data, 200
        except Exception as e:
            error_data = {
                'status_code': 0,  # Error
                'msg': "error",
                'description': str(e)
            }
            return error_data, 400