sina.com.                 IN SOA  root.sina.com. mail.sina.com. (
                                    2016073101 ; serial
                                    3600 ; refresh (1 hour)
                                    3600   ; retry (30 minutes)
                                    3600  ; expire (1 week)
                                    3600 ; mininum (1 day)
                                     )
$ORIGIN sina.com.

www         180       A      1.1.1.1
