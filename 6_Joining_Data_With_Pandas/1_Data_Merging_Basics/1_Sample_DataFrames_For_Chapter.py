# Sample DataFrames used in these exercises

# taxi_owners  DataFrame
#         rid   vid                          owner                               address    zip
# 0     T6285  6285                 AGEAN TAXI LLC                   4536 N. ELSTON AVE.  60630
# 1     T4862  4862                   MANGIB CORP.                5717 N. WASHTENAW AVE.  60659
# 2     T1495  1495                  FUNRIDE, INC.                   3351 W. ADDISON ST.  60618
# 3     T4231  4231                   ALQUSH CORP.                 6611 N. CAMPBELL AVE.  60645
# 4     T5971  5971                 EUNIFFORD INC.                   3351 W. ADDISON ST.  60618
# 5     T3311  3311            AHMED VOHRA CAB CO.                   9696 W. FOSTER AVE.  60656
# 6     T3761  3761                TROJAN CAB CORP                   9696 W. FOSTER AVE.  60656
# 7     T1918  1918                     HARRAH INC                 2601 W. PETERSON AVE.  60659
# 8     T3446  3446              LUNA TAXICAB INC.                   3351 W. ADDISON ST.  60618
# 9     T1617  1617            AMPLE SUN CAB CORP.                   2617 S. WABASH AVE.  60616
# 10    T3867  3867                 T-BAR TAXI LLC                  2532 W. WARREN BLVD.  60612
# 11    T1236  1236                       YC20 LLC                   3351 W. ADDISON ST.  60618
# 12    T2164  2164                COMPUTER CAB CO                 4626 W. CORNELIA AVE.  60641
# 13    T3399  3399        HAFFARY & BAIICHE CORP.                 2601 W. PETERSON AVE.  60659
# 14    T6324  6324               IAMA EXPRESS INC                   3351 W. ADDISON ST.  60618
# 15    T5494  5494                  NBA TAXI INC.                 4020 W. GLENLAKE AVE.  60646
# 16     T227   227                 BABY CAB CORP.                   2617 S. WABASH AVE.  60616
# 17    T1609  1609                    MG & KA INC                   3351 W. ADDISON ST.  60618
# 18    T1447  1447     SNOWSTORM II HACKING CORP.                   2617 S. WABASH AVE.  60616
# 19     T468   468                  M ASANTE INC.                   3351 W. ADDISON ST.  60618
# 20     T799   799                  ALAM ENT INC.                  5501 N. MELVINA AVE.  60630
# 21    T5694  5694                    RAR CAB LLC                   9696 W. FOSTER AVE.  60656
# 22    T2658  2658            WHITE STAR TAXI INC                   3351 W. ADDISON ST.  60618
# 23    T6232  6232                   VOYAGER CORP                      5416 N. BROADWAY  60640
# 24    T4961  4961             EDUARDO MANZANAREZ                   3351 W. ADDISON ST.  60618
# 25     T742   742                     HAAEK CORP                     6550 N. CLARK ST.  60626
# 26    T3595  3595                 JULY CAB CORP.                   2617 S. WABASH AVE.  60616
# 27    T3747  3747                COHEN CAB CORP.                  5416 N. BROADWAY ST.  60640
# 28    T1484  1484              AQUARIUS CAB INC.                  6500 N. WESTERN AVE.  60645
# 29     T604   604                SUSAN CAB CORP.                   2617 S. WABASH AVE.  60616
# ...     ...   ...                            ...                                   ...    ...
# 3489  T2313  2313                      SHAHI INC                   9696 W. FOSTER AVE.  60656
# 3490  T4540  4540                ELSTON FOUR LLC                   3351 W. ADDISON ST.  60618
# 3491   T716   716                AB TAXI COMPANY                   3351 W. ADDISON ST.  60618
# 3492   T251   251                 M'ZAIR CAB INC                 4626 W. CORNELIA AVE.  60641
# 3493  T3016  3016  DRAKE GLOBAL ENTERPRISES INC.                 2945 W. PETERSON AVE.  60659
# 3494  T3772  3772               AT HANIBBOC INC.                  5765 N. LINCOLN AVE.  60659
# 3495  T2312  2312            SAMUEL WUBET TAMENE                  2243 W. FARWELL AVE.  60645
# 3496  T3672  3672               SAHIWAL CAB CORP                   3351 W. ADDISON ST.  60618
# 3497  T3804  3804                    NECT 27 LLC                  6500 N. WESTERN AVE.  60645
# 3498  T1883  1883      ZILMETTA CAB INCORPORATED                 2800 W. PETERSON AVE.  60659
# 3499  T1330  1330              CHICAGO SEVEN INC                   2617 S. WABASH AVE.  60616
# 3500  T6195  6195              AQRAMAR TAXI INC.                 4301 W. MONTROSE AVE.  60641
# 3501  T4033  4033                  ANY CAB CORP.                   4536 N. ELSTON AVE.  60630
# 3502  T3696  3696               FELIX MANZANAREZ                 2945 W. PETERSON AVE.  60659
# 3503  T6883  6883                       MOMO LLC                   4536 N. ELSTON AVE.  60630
# 3504  T3784  3784     CHICAGO MEDALLION ONE LLC.                   9696 W. FOSTER AVE.  60656
# 3505  T5277  5277             SNOWBLIND CAB CORP                   2617 S. WABASH AVE.  60616
# 3506  T5732  5732                   COONS CAB CO  8001 S. DR MARTIN LUTHER KING JR DR.  60619
# 3507   T912   912              CHICAGO SEVEN INC                   2617 S. WABASH AVE.  60616
# 3508  T3583  3583                   KAUSAR, INC.                 4626 W. CORNELIA AVE.  60641
# 3509  T6215  6215               CHICAGO TAXI INC                  6500 N. WESTERN AVE.  60645
# 3510  T5581  5581                  AMRIT CAB CO.                 4118 W. LAWRENCE AVE.  60630
# 3511  T1281  1281                    NECT 26 LLC                  6500 N. WESTERN AVE.  60645
# 3512  T5778  5778                  SALSABIL INC.                 4626 W. CORNELIA AVE.  60641
# 3513  T1421  1421            EC CHICAGO TAXI LLC                   4536 N. ELSTON AVE.  60630
# 3514  T4453  4453                IMAGIN CAB CORP                   3351 W. ADDISON ST.  60618
# 3515   T121   121               TRIBECA CAB CORP                   4536 N. ELSTON AVE.  60630
# 3516  T3465  3465               AMIR EXPRESS INC                   3351 W. ADDISON ST.  60618
# 3517  T1962  1962               KARY CAB COMPANY                   4707 N. KENTON AVE.  60630
# 3518  T1031  1031                    NECT 42 LLC                  6500 N. WESTERN AVE.  60645
#
# [3519 rows x 5 columns]



# taxi_veh DataFrame

#        vid     make          model  year               fuel_type                               owner
# 0     2767   TOYOTA          CAMRY  2013                  HYBRID                      SEYED M. BADRI
# 1     1411   TOYOTA           RAV4  2017                  HYBRID                         DESZY CORP.
# 2     6500   NISSAN         SENTRA  2019                GASOLINE                      AGAPH CAB CORP
# 3     2746   TOYOTA          CAMRY  2013                  HYBRID                 MIDWEST CAB CO, INC
# 4     5922   TOYOTA          CAMRY  2013                  HYBRID                      SUMETTI CAB CO
# 5     6537     FORD         ESCAPE  2012                  HYBRID                 BLUE EYES CAB CORP.
# 6     1461   TOYOTA          PRIUS  2013                  HYBRID                         SKAMPA INC.
# 7     3524   TOYOTA          CAMRY  2013                  HYBRID                          EAJJU INC.
# 8     5916   TOYOTA          CAMRY  2014                  HYBRID                      3860 TAXI CORP
# 9     5904   TOYOTA          CAMRY  2015                  HYBRID         SARDAR BAIG ENTERPRISES INC
# 10    1513   TOYOTA          CAMRY  2013                  HYBRID                 RIDGEVIEW CAB CORP.
# 11    2238   TOYOTA           RAV4  2015                GASOLINE                        LEROY RAMSAY
# 12    5151   TOYOTA          CAMRY  2011                  HYBRID                         BATUNDE INC
# 13    1154   TOYOTA          CAMRY  2019                  HYBRID                    MM & SS TAXI INC
# 14    5338   TOYOTA          CAMRY  2013                  HYBRID                     SAHARAN CAB INC
# 15    4154   TOYOTA          PRIUS  2011                  HYBRID                        ILYAS & SONS
# 16     652   TOYOTA          CAMRY  2015                  HYBRID                       Z & Z CAB INC
# 17    1363   TOYOTA         SIENNA  2019                GASOLINE                        1363 CAB INC
# 18    3602   TOYOTA          CAMRY  2014                  HYBRID                        TRANZIT INC.
# 19    1778   TOYOTA          CAMRY  2014                  HYBRID                       A RATTANI INC
# 20    6205     FORD         ESCAPE  2011                  HYBRID              CHOICE ENTERPRISE INC.
# 21    4746   TOYOTA          CAMRY  2017                  HYBRID                     M & W TAXI INC.
# 22    1640     FORD         ESCAPE  2012                  HYBRID                 AMPLE SUN CAB CORP.
# 23    3230   TOYOTA          PRIUS  2012                  HYBRID               FULL MOON CAB COMPANY
# 24      80   TOYOTA          CAMRY  2016                  HYBRID                     MCCAB XII CORP.
# 25    5347     FORD         ESCAPE  2012                  HYBRID             CHICAGO POLO VIII, INC.
# 26    6658   NISSAN         ALTIMA  2017                GASOLINE                      SOURCE CAB CO.
# 27    6955    DODGE  GRAND CARAVAN  2013  COMPRESSED NATURAL GAS                   MIRZASULEMAN CORP
# 28    2182   TOYOTA          CAMRY  2013                  HYBRID                   SAMGATE ACKERPATT
# 29    5359   TOYOTA          CAMRY  2013                  HYBRID                  ASSYRIAN TRANS INC
# ...    ...      ...            ...   ...                     ...                                 ...
# 3489  4330   NISSAN          NV200  2015                  HYBRID                     GYPSY CAB CORP.
# 3490  6676   TOYOTA         SIENNA  2020                GASOLINE                         ALMAHDI INC
# 3491  6598   TOYOTA          CAMRY  2014                  HYBRID                CHITOWN CAB INC # II
# 3492  6728  HYUNDAI        ELANTRA  2018                GASOLINE                      SAMOS CAB CORP
# 3493  6686     FORD         ESCAPE  2012                  HYBRID                     GYPSY CAB CORP.
# 3494  6570   TOYOTA          PRIUS  2016                  HYBRID                   BETHEL MOKSON INC
# 3495   688   TOYOTA         SIENNA  2019                GASOLINE                         QUOMASS INC
# 3496   814    DODGE        CARAVAN  2016                GASOLINE                      MCCAB IX CORP.
# 3497   836   TOYOTA          PRIUS  2014                  HYBRID                    JOHNS CABS CORP.
# 3498   816   TOYOTA          CAMRY  2014                  HYBRID                   DEFIANCE TAXI LLC
# 3499   860  HYUNDAI        ELANTRA  2018                GASOLINE                      ZEUS CAB CORP.
# 3500   702   TOYOTA           RAV4  2017                  HYBRID                       Z & Z CAB INC
# 3501   726   TOYOTA          CAMRY  2014                  HYBRID                    SKYWARD CAB INC.
# 3502  6734   TOYOTA          CAMRY  2016                  HYBRID  TAXI MEDALLION GROUP LLC-SERIES 35
# 3503  6750   TOYOTA          CAMRY  2016                  HYBRID  TAXI MEDALLION GROUP LLC-SERIES 37
# 3504    71   TOYOTA          CAMRY  2013                  HYBRID                           PED 4 LLC
# 3505  4496   TOYOTA         SIENNA  2020                GASOLINE                        FAIZ CAB INC
# 3506  4448   TOYOTA          PRIUS  2013                  HYBRID                       BMC CAB CORP.
# 3507   934   TOYOTA         SIENNA  2018                GASOLINE                         TAXI ME INC
# 3508   958     FORD         ESCAPE  2010                  HYBRID                          NECT 47LLC
# 3509  4524   TOYOTA          CAMRY  2017                  HYBRID                       CAROL CAB CO.
# 3510  4428   TOYOTA         SIENNA  2015                GASOLINE                  WONDER CAB COMPANY
# 3511  6933     FORD          C-MAX  2013                  HYBRID           SANTORINI THREE CAB CORP.
# 3512  4814   TOYOTA          CAMRY  2017                  HYBRID  TAXI MEDALLION GROUP LLC SERIES 27
# 3513  4820   TOYOTA          CAMRY  2016                  HYBRID  TAXI MEDALLION GROUP LLC SERIES 28
# 3514  5902   TOYOTA          CAMRY  2013                  HYBRID                           SAFAR INC
# 3515  1407  HYUNDAI        ELANTRA  2018                GASOLINE                   MYKONOS CAB CORP.
# 3516   854   TOYOTA          CAMRY  2012                  HYBRID                     JOELIZ CORP INC
# 3517  6274   TOYOTA          CAMRY  2012                  HYBRID                         A K O S INC
# 3518  4675     FORD         ESCAPE  2011               FLEX FUEL                          MAJAZ CORP
#
# [3519 rows x 6 columns]


# wards

#    ward                   alderman                            address    zip
# 0     1         Proco "Joe" Moreno          2058 NORTH WESTERN AVENUE  60647
# 1     2              Brian Hopkins         1400 NORTH  ASHLAND AVENUE  60622
# 2     3                 Pat Dowell            5046 SOUTH STATE STREET  60609
# 3     4           William D. Burns    435 EAST 35TH STREET, 1ST FLOOR  60616
# 4     5         Leslie A. Hairston              2325 EAST 71ST STREET  60649
# 5     6         Roderick T. Sawyer   8001 S. MARTIN LUTHER KING DRIVE  60619
# 6     7        Gregory I. Mitchell              2249 EAST 95TH STREET  60617
# 7     8         Michelle A. Harris    8539 SOUTH COTTAGE GROVE AVENUE  60619
# 8     9           Anthony A. Beale                34 EAST 112TH PLACE  60628
# 9    10      Susan Sadlowski Garza           10500 SOUTH EWING AVENUE  60617
# 10   11     Patrick Daley Thompson          3659 SOUTH HALSTED STREET  60609
# 11   12            George Cardenas           3476 SOUTH ARCHER AVENUE  60608
# 12   13                Marty Quinn            6500 SOUTH PULASKI ROAD  60629
# 13   14            Edward M. Burke              2650 WEST 51ST STREET  60632
# 14   15           Raymond A. Lopez              1650 WEST 63RD STREET  60636
# 15   16            Toni L. Foulkes              3045 WEST 63RD STREET  60629
# 16   17             David H. Moore          7313 SOUTH ASHLAND AVENUE  60636
# 17   18          Derrick G. Curtis            8359 SOUTH PULASKI ROAD  60652
# 18   19          Matthew J. O'Shea         10400 SOUTH WESTERN AVENUE  60643
# 19   20          Willie B. Cochran    6357 SOUTH COTTAGE GROVE AVENUE  60637
# 20   21    Howard B. Brookins, Jr.  9011 SOUTH ASHLAND AVENUE, UNIT B  60620
# 21   22              Ricardo Munoz        2500 SOUTH ST. LOUIS AVENUE  60623
# 22   23        Michael R. Zalewski           6247 SOUTH ARCHER AVENUE  60638
# 23   24         Michael Scott, Jr.           1158 SOUTH KEELER AVENUE  60624
# 24   25       Daniel "Danny" Solis      1800 SOUTH BLUE ISLAND AVENUE  60608
# 25   26          Roberto Maldonado          2511 WEST DIVISION STREET  60622
# 26   27        Walter Burnett, Jr.             4 NORTH WESTERN AVENUE  60612
# 27   28             Jason C. Ervin              2602 WEST 16TH STREET  60612
# 28   29           Chris Taliaferro             6272 WEST NORTH AVENUE  60639
# 29   30          Ariel E. Reyboras        3559 NORTH MILWAUKEE AVENUE  60641
# 30   31  Milagros "Milly" Santiago            2521 NORTH PULASKI ROAD  60639
# 31   32           Scott Waguespack         2657 NORTH CLYBOURN AVENUE  60614
# 32   33               Deborah Mell         3001 WEST IRVING PARK ROAD  60618
# 33   34           Carrie M. Austin              507 WEST 111TH STREET  60628
# 34   35        Carlos Ramirez-Rosa           2710 NORTH SAWYER AVENUE  60647
# 35   36           Gilbert Villegas                 6934 WEST DIVERSEY  60607
# 36   37              Emma M. Mitts           4924 WEST CHICAGO AVENUE  60651
# 37   38           Nicholas Sposato          3821  NORTH HARLEM AVENUE  60634
# 38   39           Margaret Laurino          4404 WEST LAWRENCE AVENUE  60630
# 39   40        Patrick J. O'Connor          5850 NORTH LINCOLN AVENUE  60659
# 40   41      Anthony V. Napolitano           7442 NORTH HARLEM AVENUE  60631
# 41   42             Brendan Reilly   325 WEST HURON STREET, SUITE 510  60654
# 42   43             Michelle Smith          2523 NORTH HALSTED STREET  60614
# 43   44                 Tom Tunney        3223 NORTH SHEFFIELD AVENUE  60657
# 44   45              John S. Arena        4754 NORTH MILWAUKEE AVENUE  60630
# 45   46            James Cappleman         4544 NORTH BROADWAY AVENUE  60640
# 46   47                Ameya Pawar          4243 NORTH LINCOLN AVENUE  60618
# 47   48             Harry Osterman         5533 NORTH BROADWAY AVENUE  60640
# 48   49                  Joe Moore        7356 NORTH GREENVIEW AVENUE  60626
# 49   50       Debra L. Silverstein    2949 WEST DEVON AVENUE, SUITE A  60659


# census

#    ward  pop_2000  pop_2010 change                                            address    zip
# 0     1     52951     56149     6%                        2765 WEST SAINT MARY STREET  60647
# 1     2     54361     55805     3%                           WM WASTE MANAGEMENT 1500  60622
# 2     3     40385     53039    31%                                17 EAST 38TH STREET  60653
# 3     4     51953     54589     5%            31ST ST HARBOR BUILDING LAKEFRONT TRAIL  60653
# 4     5     55302     51455    -7%            JACKSON PARK LAGOON SOUTH CORNELL DRIVE  60637
# 5     6     54989     52341    -5%                               150 WEST 74TH STREET  60636
# 6     7     54593     51581    -6%                          8549 SOUTH OGLESBY AVENUE  60617
# 7     8     54039     51687    -4%                         1346-1352 EAST 75TH STREET  60649
# 8     9     52008     51519    -1%                 11039-11059 SOUTH WENTWORTH AVENUE  60628
# 9    10     56613     51535    -9%                               10534 SOUTH AVENUE F  46394
# 10   11     64228     51497   -20%                            943-947 WEST 14TH PLACE  60607
# 11   12     68922     52235   -24%                         CP 46 STEVENSON EXPRESSWAY  60632
# 12   13     64382     53722   -17%                    SOUTH RAMP SOUTH LARAMIE AVENUE  60638
# 13   14     80143     54031   -33%                              4540 WEST 51ST STREET  60632
# 14   15     56057     51501    -8%    CHICAGO FIRE DEPARTMENT ENGINE COMPANY 123 2215  60632
# 15   16     50205     51954     3%                             6036 SOUTH WOOD STREET  60636
# 16   17     49264     51846     5%                       7216 SOUTH WINCHESTER AVENUE  60636
# 17   18     55043     52992    -4%                          3286 WEST COLUMBUS AVENUE  60652
# 18   19     54546     51525    -6%                        9999 SOUTH FRANCISCO AVENUE  60805
# 19   20     51854     52372     1%                     DAN RYAN EXPRESSWAY PARK MANOR  60621
# 20   21     51751     51632     0%                     8852-8854 SOUTH EMERALD AVENUE  60620
# 21   22     59734     53515   -10%                              4233 WEST 36TH STREET  60632
# 22   23     63691     53728   -16%  CHICAGO MIDWAY INTERNATIONAL AIRPORT WEST 62ND...  60629
# 23   24     50879     54909     8%                       1635 SOUTH CHRISTIANA AVENUE  60623
# 24   25     55954     54539    -3%                      1632-1746 SOUTH MILLER STREET  60608
# 25   26     56841     53516    -6%             LITTLE CUBS FIELD COMFORT STATION 1400  60622
# 26   27     61287     52939   -14%                      2151-2153 WEST CHICAGO AVENUE  60651
# 27   28     49423     55199    12%                        RML SPECIALTY HOSPITAL 3435  60624
# 28   29     61949     55267   -11%                        1241 NORTH RIDGELAND AVENUE  60302
# 29   30     72698     55560   -24%                          5118 WEST FLETCHER STREET  60641
# 30   31     65045     53724   -17%                          2854 NORTH KEATING AVENUE  60641
# 31   32     57204     55184    -4%                        2901 NORTH WASHTENAW AVENUE  60618
# 32   33     63695     55598   -13%                    4041-4043 NORTH RICHMOND STREET  60625
# 33   34     49922     51599     3%                    11544-11546 SOUTH PEORIA STREET  60827
# 34   35     57588     55281    -4%                           3634 WEST BELMONT AVENUE  60618
# 35   36     63376     54766   -14%                       2918 NORTH RUTHERFORD AVENUE  60634
# 36   37     56120     51538    -8%                         4738-4748 WEST RICE STREET  60651
# 37   38     66011     56001   -15%                    7307-7331 WEST IRVING PARK ROAD  60706
# 38   39     64291     55882   -13%                  QUEEN OF ALL SAINTS BASILICA 6280  60646
# 39   40     58652     55319    -6%                         5536 NORTH ARTESIAN AVENUE  60645
# 40   41     56127     55991     0%                          1652 SOUTH CLIFTON AVENUE  60068
# 41   42     68102     55870   -18%                          410-420 WEST GRAND AVENUE  60654
# 42   43     57668     56170    -3%                              LINCOLN PARK ZOO 2001  60614
# 43   44     58758     56058    -5%                         507-513 WEST ALDINE AVENUE  60657
# 44   45     60653     55967    -8%       CONGREGATIONAL CHURCH OF JEFFERSON PARK 5320  60630
# 45   46     56587     53784    -5%                 UPTOWN BROADWAY BUILDING 4743-4763  60640
# 46   47     52108     55074     6%                           2153 WEST BERTEAU AVENUE  60618
# 47   48     56246     55014    -2%                         1025 WEST HOLLYWOOD AVENUE  60660
# 48   49     59435     54633    -8%                             1426 WEST ESTES AVENUE  60645
# 49   50     62383     55809   -11%                       2638 WEST NORTH SHORE AVENUE  60645