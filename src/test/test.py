#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import datetime
import sys
import time 

class Enrichment:
    HELP_MSG = "Enrichment: Make enrichment for ORDER DBS.\n" \
               "Usage: ./make_enrichment.py [DATE=YYYYMMDD]\n" \
               "Required Environment Variables:" \
               "\n\t$MAIN_DATA_DIR;\n\t$MAIN_ONE_TICK_DIR;\n\t$MAIN_LOG_DIR;\n\t$BESTEX_PACK;" \
               "\n\t$MAIN_CLIENT_DIR;\n\t$ORDERS_DBS;"\
               "\nIf date isn't specfied DATE = TODAY (is the greatest day I ever know) - 1"
    def __init__(self, main_data_dir, main_onetick_dir, bestex_pack,
                 main_client_dir, main_log_dir, date, verbose=False):
        self.main_data_dir = main_data_dir
        self.main_onetick_dir = main_onetick_dir
        self.bestex_pack = bestex_pack
        self.main_client_dir = main_client_dir
        self.main_log_dir = main_log_dir
        self.verbose = verbose
        self.current_date = time.strftime("%Y%m%d")
        self.date = date

    def make_enrichment(self, databases, nbbo, nyse, ench_db, offset_csv, csv_db, timezone, otq_file, spread_check_threshhold, window_before, window_after):
        starttime = self.date + "000000";
        endtime = self.date + "235959";
        otq_file = self.bestex_pack + otq_file;
        for database in databases:
            order_db = "S_ORDERS_" + database + "::ORDER";
            log = self.main_log_dir + "/small_order_enrichment." + database + "." + self.date + ".log 2>&1";
            print ("Order DB: %s\n") % (order_db);
            otq_params = "SPREAD_CHECK_THRESHOLD=" + spread_check_threshhold + ",";
            otq_params = otq_params + "CONSOLIDATED_QUOTE_DB=" + nbbo + ",PRIMARY_QUOTE_DB=" + nbbo + ",";
            otq_params = otq_params + "WINDOW_BEFORE=" + window_before + ",WINDOW_AFTER=" + window_after + ",";
            otq_params = otq_params + "OFFSETS_CSV=" + offset_csv + ",OUTPUT_DB=" + ench_db + ",ORDER_DB=" + order_db + ",";
            otq_params = otq_params + "PATTERN=%,";
            otq_params = otq_params + "CSV_DB=" + csv_db + ",TRD_DB=" + nyse + ",";
            otq_params = otq_params + "DATE=" + self.date + " -s " + starttime + " -e " + endtime + " ";
            otq_params = otq_params + "-timezone " + timezone + " -batch_size 16 -max_concurrency 8 -process_dbs_concurrently true";
            command = self.main_onetick_dir + "/bin/tickdb_query.exe -context REMOTE -otq_file " + otq_file + " -otq_params " + otq_params;
            print ("command: %s\n") % (command);
            print ("log: %s\n") % (log);
            os.system(command + " >> " + log);
            time.sleep(60);


def main(argv):
    if os.environ["MAIN_DATA_DIR"] == '' or os.environ["BESTEX_PACK"] == '' or os.environ["MAIN_CLIENT_DIR"] == '':
        print ("[Error]: Empty environment variables!")
        return -1

    date = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y%m%d")
    if len(argv) > 1:
        date = argv[1]
    # print "date: %s\n" % (date)
    databases = os.environ["ORDERS_DBS"].split(',')
    nbbo = "TAQ_NBBO::NBBO";
    nyse = "NYSE_TAQ::TRD";
    ench_db = "S_ORDERS_ENHANCED";
    offset_csv = "offsets.cfg";
    csv_db = "BESTEX";
    timezone = "GMT";
    otq_file = "/otqs/analytics/SmallOrderEnrichment.otq::SmallOrderEnrichment";
    spread_check_threshhold = "500.00";
    window_before = "10";
    window_after = "0.5";
    enrichment = Enrichment(os.environ["MAIN_DATA_DIR"], os.environ["MAIN_ONE_TICK_DIR"],
                      os.environ["BESTEX_PACK"], os.environ["MAIN_CLIENT_DIR"],
                      os.environ["MAIN_LOG_DIR"], date, True)
    enrichment.make_enrichment(databases, nbbo, nyse, ench_db, offset_csv, csv_db, timezone, otq_file,
                      spread_check_threshhold, window_before, window_after)
        
    return 0

def test():
    print (lambda x, y: x + y, filter(lambda x: x % 2, map(lambda x: x * x, range (10 ** 6))))
    print (sum(x * x for x in range(1, 10 ** 6, 2)))
    print (lambda x, y: x + y, filter(lambda x: x % 2, map(lambda x: x * x, range (10 ** 6)))) == sum(x * x for x in range(1, 10 ** 6, 2))

if __name__ == '__main__':
    test()
