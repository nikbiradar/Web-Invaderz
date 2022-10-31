python3 DB_create.py
websites=(
#MOVIES
   "https://www.imdb.com/chart/top/" 
    "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
#INDIAN MOVIES BY LANGUAGE
    "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=JASDFA3EEJYZNQHE9WG6&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_hd"
    "https://www.imdb.com/india/top-rated-tamil-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=57b6cfe5-784a-4764-bb68-72ed85c2961e&pf_rd_r=JASDFA3EEJYZNQHE9WG6&pf_rd_s=center-2&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_ta_hd"
    "https://www.imdb.com/india/top-rated-telugu-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=96154ad2-ff9d-45d3-bb50-7a39474f5d8e&pf_rd_r=JASDFA3EEJYZNQHE9WG6&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_te_hd"
    "https://www.imdb.com/india/top-rated-malayalam-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4a339a9f-392d-42d2-8912-566ffdc1152b&pf_rd_r=JASDFA3EEJYZNQHE9WG6&pf_rd_s=center-5&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_ml_hd"
#TV SHOWS
    "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv"

)
python3 add_info.py "https://www.imdb.com/chart/top/"
python3 add_info.py "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
python3 add_info.py "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=JASDFA3EEJYZNQHE9WG6&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_hd"
python3 add_info.py "https://www.imdb.com/india/top-rated-tamil-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=57b6cfe5-784a-4764-bb68-72ed85c2961e&pf_rd_r=JASDFA3EEJYZNQHE9WG6&pf_rd_s=center-2&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_ta_hd"
for website in ${websites[@]}; do
  python3 add_info.py $website
done
