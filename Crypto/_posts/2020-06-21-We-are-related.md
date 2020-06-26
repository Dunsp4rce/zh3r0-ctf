---
layout: post
title: "We are related"
author: "raghul-rajasekar"
---

## Question

I can help you send related messages can you out what it is?  
nc crypto.zh3r0.ml 9841

## Solution

On running `nc crypto.zh3r0.ml 9841`, we get the following prompt:
![RSA prompt]({{ site.baseurl }}/images/we_are_related.png)
The public key returned by the prompt is in [ASN.1 DER format](https://lapo.it/asn1js/). Decoding it gives us:
```
n = 19180711545893176513037550390323379574821852830665661812056678865741809891967598330424432450065638550340708416772232861627803383996685973692319978144111094705678356718069839745329804369923049623077146724976343425793942969144731442443607177966505595110345695314223998207352543996470777991272166737723490287258351016452097039979125039319504321174407700539531877444075872453220474913463319033875264101011295681676774076367210997858399851393634010112304767318681335454946488666538950765836709367621997962434256967765320251658524109362889423421160554230180542246491892887129152380892721807921025298941063392821275387956851
e = 3
```
These are the values of `n` and `e` for RSA. Interestingly, the value of `e` is very low. Based on the problem statement, the intended solution was to use the [**Franklin-Reiter related-message attack**](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Franklin-Reiter_related-message_attack). However, I solved it in a slightly different way, by sending three messages with `txt` as `'0'`, `'1'` and `'2'` respectively. Thus, the three messages encrypted are `m0 = flag + '0'`, `m1 = flag + '1'` and `m2 = flag + '2'`.  The corresponding ciphertexts received are <code>c0 ≡ m0<sup>3</sup> mod n</code>, <code>c1 ≡ m1<sup>3</sup> mod n</code> and <code>c2 ≡ m2<sup>3</sup> mod n</code>. Since `m0 = m1 - 1` and `m2 = m1 + 1`, we get `6*m1 ≡ c0 + c2 - 2*c1 mod n`.

After solving this, we get
```
m1 = 21629562076244534444303488461223071010548114550354514970028717986950416686920316463397978760310140905489337755725363011614509386441355772286271153257012649008495272596701703740750134512758262801971417412780324410142458963662822945134345945728656790759706540853989929425583870615345557417412960682959465981275433575053005642501889534294718262627799906591256113
```
Converting to ASCII, we get the message to be
```
RSA is secure and all but the only thing I want to say is zh3r0{Hey_y0u_Sh0u1dn't_S3nd_r3l4ted_m3ssag3s_0r_h4v3_shot_p4ddings_wh3n_e_1s_sm411!!!!!}.1
```
(the `1` at the end is the value of `txt` that we gave as input for `m1`).

Flag: 
```
zh3r0{Hey_y0u_Sh0u1dn't_S3nd_r3l4ted_m3ssag3s_0r_h4v3_shot_p4ddings_wh3n_e_1s_sm411!!!!!}
```
