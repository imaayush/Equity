import redis
import os
from constants import SHOW_NUMBER_COMPANIES

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')


class RedisServices():
    def __init__(self):
        """Connect to redis"""
        self.redis = redis.from_url(redis_url)

    def post(self, companies_details):
        """Store companies details to redis database"""
        for company_details in companies_details:
            self.redis.hmset(company_details.get('SC_NAME'), company_details)

        for index_num in range(0, SHOW_NUMBER_COMPANIES):
            self.redis.set(
                index_num, companies_details[index_num].get('SC_NAME'))

    def get_top_ten(self):
        """Return to ten entries from redis"""
        names = [self.redis.get(index_num)
                 for index_num in range(0, SHOW_NUMBER_COMPANIES)]
        companies_details = [self.redis.hgetall(name) for name in names]
        return companies_details

    def get_by_name(self, name):
        """Search company for given name"""
        return self.redis.hgetall(name.upper())
