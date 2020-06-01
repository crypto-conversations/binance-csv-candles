# binance-csv-candles

Fetch Binance BTC, ETH and USDT market data and create/update `csv` candle files.
Files are stored in `./data/binance/{timeframe}`. Timeframe can be anything like `1d`, `1h`, etc.

## Usage

The first time and then every time you want to update the data in your `csv` files, just run it like this:

```bash
$ python fetch_and_update_candles.py --timeframe 1d
```
## Manual

Each `csv` file contains 5 columns:
* date (unix timestamp),
* open,
* high,
* low,
* close,
* volume

## Results

Hourly timeframe example (`1h`): there are 350+ pairs (files) which amount to 500+ MB of data for `1h` and 15MB for `1d`, that is why the first run will take some time.

```bash
$ ls data/binance/1h
ADA-BTC.csv       BTG-BTC.csv       ENJ-BTC.csv       IOTA-BTC.csv      NAS-BTC.csv       RDN-BTC.csv       VET-BTC.csv
ADA-ETH.csv       BTS-BTC.csv       ENJ-ETH.csv       IOTA-ETH.csv      NAS-ETH.csv       REN-BTC.csv       VET-ETH.csv
ADA-USDT.csv      BTS-USDT.csv      ENJ-USDT.csv      IOTA-USDT.csv     NAV-BTC.csv       REN-USDT.csv      VET-USDT.csv
ADX-BTC.csv       BTT-USDT.csv      EOS-BTC.csv       IOTX-BTC.csv      NCASH-ETH.csv     REP-BTC.csv       VIA-BTC.csv
ADX-ETH.csv       BUSD-USDT.csv     EOS-ETH.csv       IOTX-ETH.csv      NEBL-BTC.csv      REP-ETH.csv       VIB-BTC.csv
AE-BTC.csv        CDT-BTC.csv       EOS-USDT.csv      IOTX-USDT.csv     NEBL-ETH.csv      REQ-BTC.csv       VIB-ETH.csv
AE-ETH.csv        CDT-ETH.csv       ERD-BTC.csv       KAVA-BTC.csv      NEO-BTC.csv       RLC-BTC.csv       VIBE-BTC.csv
AGI-BTC.csv       CELR-BTC.csv      ERD-USDT.csv      KAVA-USDT.csv     NEO-ETH.csv       RLC-ETH.csv       VITE-BTC.csv
AION-BTC.csv      CELR-USDT.csv     ETC-BTC.csv       KEY-ETH.csv       NEO-USDT.csv      RLC-USDT.csv      VITE-USDT.csv
AION-ETH.csv      CHR-BTC.csv       ETC-ETH.csv       KEY-USDT.csv      NKN-BTC.csv       RVN-BTC.csv       WABI-BTC.csv
AION-USDT.csv     CHR-USDT.csv      ETC-USDT.csv      KMD-BTC.csv       NKN-USDT.csv      RVN-USDT.csv      WAN-BTC.csv
ALGO-BTC.csv      CHZ-BTC.csv       ETH-BTC.csv       KMD-ETH.csv       NPXS-ETH.csv      SC-BTC.csv        WAN-ETH.csv
ALGO-USDT.csv     CHZ-USDT.csv      ETH-USDT.csv      KNC-BTC.csv       NPXS-USDT.csv     SC-ETH.csv        WAN-USDT.csv
AMB-BTC.csv       CMT-BTC.csv       EUR-USDT.csv      KNC-ETH.csv       NULS-BTC.csv      SKY-BTC.csv       WAVES-BTC.csv
ANKR-BTC.csv      CMT-ETH.csv       EVX-BTC.csv       LEND-BTC.csv      NULS-ETH.csv      SNGLS-BTC.csv     WAVES-ETH.csv
ANKR-USDT.csv     CND-BTC.csv       EVX-ETH.csv       LEND-ETH.csv      NULS-USDT.csv     SNM-BTC.csv       WAVES-USDT.csv
APPC-BTC.csv      COCOS-USDT.csv    FET-BTC.csv       LEND-USDT.csv     NXS-BTC.csv       SNT-BTC.csv       WIN-USDT.csv
ARDR-BTC.csv      COS-BTC.csv       FET-USDT.csv      LINK-BTC.csv      OAX-BTC.csv       SNT-ETH.csv       WPR-BTC.csv
ARDR-USDT.csv     COS-USDT.csv      FTM-BTC.csv       LINK-ETH.csv      OGN-BTC.csv       SOL-BTC.csv       WRX-BTC.csv
ARK-BTC.csv       COTI-BTC.csv      FTM-USDT.csv      LINK-USDT.csv     OGN-USDT.csv      STEEM-BTC.csv     WRX-USDT.csv
ARN-BTC.csv       COTI-USDT.csv     FTT-BTC.csv       LOOM-BTC.csv      OMG-BTC.csv       STEEM-ETH.csv     WTC-BTC.csv
ARN-ETH.csv       CTSI-BTC.csv      FTT-USDT.csv      LOOM-ETH.csv      OMG-ETH.csv       STORJ-BTC.csv     WTC-ETH.csv
ARPA-BTC.csv      CTSI-USDT.csv     FUEL-BTC.csv      LRC-BTC.csv       OMG-USDT.csv      STORJ-ETH.csv     WTC-USDT.csv
ARPA-USDT.csv     CTXC-BTC.csv      FUN-BTC.csv       LRC-ETH.csv       ONE-BTC.csv       STORM-BTC.csv     XEM-BTC.csv
AST-BTC.csv       CTXC-USDT.csv     FUN-ETH.csv       LSK-BTC.csv       ONE-USDT.csv      STORM-ETH.csv     XEM-ETH.csv
ATOM-BTC.csv      CVC-BTC.csv       FUN-USDT.csv      LSK-ETH.csv       ONG-BTC.csv       STORM-USDT.csv    XLM-BTC.csv
ATOM-USDT.csv     CVC-ETH.csv       GAS-BTC.csv       LSK-USDT.csv      ONG-USDT.csv      STPT-BTC.csv      XLM-ETH.csv
BAND-BTC.csv      CVC-USDT.csv      GNT-BTC.csv       LTC-BTC.csv       ONT-BTC.csv       STPT-USDT.csv     XLM-USDT.csv
BAND-USDT.csv     DASH-BTC.csv      GNT-ETH.csv       LTC-ETH.csv       ONT-ETH.csv       STRAT-BTC.csv     XMR-BTC.csv
BAT-BTC.csv       DASH-ETH.csv      GO-BTC.csv        LTC-USDT.csv      ONT-USDT.csv      STRAT-ETH.csv     XMR-ETH.csv
BAT-ETH.csv       DASH-USDT.csv     GRS-BTC.csv       LTO-BTC.csv       OST-BTC.csv       STRAT-USDT.csv    XMR-USDT.csv
BAT-USDT.csv      DATA-BTC.csv      GTO-BTC.csv       LTO-USDT.csv      OST-ETH.csv       STX-BTC.csv       XRP-BTC.csv
BCD-BTC.csv       DATA-ETH.csv      GTO-ETH.csv       LUN-BTC.csv       PAX-USDT.csv      STX-USDT.csv      XRP-ETH.csv
BCD-ETH.csv       DATA-USDT.csv     GTO-USDT.csv      MANA-BTC.csv      PERL-BTC.csv      SYS-BTC.csv       XRP-USDT.csv
BCH-BTC.csv       DCR-BTC.csv       GVT-BTC.csv       MANA-ETH.csv      PERL-USDT.csv     TCT-BTC.csv       XTZ-BTC.csv
BCH-USDT.csv      DENT-ETH.csv      GXS-BTC.csv       MATIC-BTC.csv     PHB-BTC.csv       TCT-USDT.csv      XTZ-USDT.csv
BCPT-BTC.csv      DENT-USDT.csv     GXS-ETH.csv       MATIC-USDT.csv    PIVX-BTC.csv      TFUEL-BTC.csv     XVG-BTC.csv
BEAM-BTC.csv      DLT-BTC.csv       GXS-USDT.csv      MBL-BTC.csv       PIVX-ETH.csv      TFUEL-USDT.csv    XVG-ETH.csv
BEAM-USDT.csv     DNT-BTC.csv       HBAR-BTC.csv      MBL-USDT.csv      POA-BTC.csv       THETA-BTC.csv     XZC-BTC.csv
BLZ-BTC.csv       DOCK-BTC.csv      HBAR-USDT.csv     MCO-BTC.csv       POE-BTC.csv       THETA-ETH.csv     XZC-ETH.csv
BLZ-ETH.csv       DOCK-ETH.csv      HC-BTC.csv        MCO-ETH.csv       POLY-BTC.csv      THETA-USDT.csv    XZC-USDT.csv
BNB-BTC.csv       DOCK-USDT.csv     HC-USDT.csv       MCO-USDT.csv      POWR-BTC.csv      TNB-BTC.csv       YOYOW-BTC.csv
BNB-ETH.csv       DOGE-BTC.csv      HIVE-BTC.csv      MDA-BTC.csv       POWR-ETH.csv      TNT-BTC.csv       ZEC-BTC.csv
BNB-USDT.csv      DOGE-USDT.csv     HIVE-USDT.csv     MFT-ETH.csv       PPT-BTC.csv       TNT-ETH.csv       ZEC-ETH.csv
BNT-BTC.csv       DREP-BTC.csv      HOT-BTC.csv       MFT-USDT.csv      QKC-BTC.csv       TOMO-BTC.csv      ZEC-USDT.csv
BNT-ETH.csv       DREP-USDT.csv     HOT-ETH.csv       MITH-BTC.csv      QKC-ETH.csv       TOMO-USDT.csv     ZEN-BTC.csv
BNT-USDT.csv      DUSK-BTC.csv      HOT-USDT.csv      MITH-USDT.csv     QLC-BTC.csv       TROY-BTC.csv      ZEN-ETH.csv
BQX-BTC.csv       DUSK-USDT.csv     ICX-BTC.csv       MTH-BTC.csv       QLC-ETH.csv       TROY-USDT.csv     ZIL-BTC.csv
BQX-ETH.csv       EDO-BTC.csv       ICX-ETH.csv       MTL-BTC.csv       QSP-BTC.csv       TRX-BTC.csv       ZIL-ETH.csv
BRD-BTC.csv       EDO-ETH.csv       ICX-USDT.csv      MTL-ETH.csv       QSP-ETH.csv       TRX-ETH.csv       ZIL-USDT.csv
BRD-ETH.csv       ELF-BTC.csv       INS-BTC.csv       MTL-USDT.csv      QTUM-BTC.csv      TRX-USDT.csv      ZRX-BTC.csv
BTC-USDT.csv      ELF-ETH.csv       IOST-BTC.csv      NANO-BTC.csv      QTUM-ETH.csv      TUSD-USDT.csv     ZRX-ETH.csv
BTCDOWN-USDT.csv  ENG-BTC.csv       IOST-ETH.csv      NANO-ETH.csv      QTUM-USDT.csv     USDC-USDT.csv     ZRX-USDT.csv
BTCUP-USDT.csv    ENG-ETH.csv       IOST-USDT.csv     NANO-USDT.csv     RCN-BTC.csv       USDS-USDT.csv
```