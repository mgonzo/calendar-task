# Elasticsearch adapter
# uses elasticsearch client
from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer
from elasticsearch_dsl.connections import connections

class Event(DocType):
    class Meta:
        index = 'events'

    def create_event(json_obj):
        # validation on json_obj?
        super(Event, self).save(json_obj)
        end

    def create_events(events_list):
        # iterate list and call create_event on each
        end

    def read_event(id):
        return super.get(id)
        end
        
    def read_events(filter, order, direction):
        end

