# tools/gta_decor_models.py
"""
52 Procedural 3D Clay Models representing the 10 ecological, industrial,
historical, and cultural themes of Augusta (SR).
"""

def get_all_augusta_decor_models():
    return '''
,"valvola-spurgo"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.42,1.2,"orange",o,0,0.6,0);
  t.cylinder(0.65,0.22,"dark",o,0,1.2,0);
  t.cylinder(0.12,0.8,"rope",o,0,1.6,0);
  t.cylinder(0.55,0.12,"gold",o,0,2.0,0);
  t.ball(0.18,0.18,0.18,"gold",o,0,2.0,0);
}
,"chiatta-megara"(t,e,n){
  const o=oo(e,n,14.0);
  t.box(16,2.4,5.2,"rope",o,0,1.2,0,0.2);
  t.box(15,0.4,4.8,"dark",o,0,2.4,0);
  t.cylinder(0.35,1.2,"gold",o,-6.5,2.8,2.0);
  t.cylinder(0.35,1.2,"gold",o,6.5,2.8,2.0);
  t.cylinder(0.35,1.2,"gold",o,-6.5,2.8,-2.0);
  t.cylinder(0.35,1.2,"gold",o,6.5,2.8,-2.0);
  t.box(4.0,2.2,3.2,"cream",o,3.5,3.4,0,0.1);
}
,"gru-portuale-rossini"(t,e,n){
  const o=oo(e,n,16.0);
  t.box(3.5,12.0,3.5,"dark",o,0,6.0,0,0.2);
  t.box(18.0,1.8,2.2,"orange",o,4.0,12.6,0,0.15);
  t.cylinder(0.10,7.5,"rope",o,10.0,8.0,0);
  t.box(2.2,2.0,2.2,"cream",o,10.0,4.0,0,0.1);
}
,"salvagente-rossini"(t,e,n){
  const o=oo(e,n,1.8);
  t.cylinder(0.08,2.2,"rope",o,0,1.1,0);
  t.ball(0.65,0.65,0.16,"cream",o,0,2.0,0.1);
  t.ball(0.32,0.32,0.22,"dark",o,0,2.0,0.1);
  t.ball(0.66,0.22,0.18,"orange",o,0,2.0,0.1);
}
,"pompa-idrovora"(t,e,n){
  const o=oo(e,n,2.5);
  t.box(2.4,1.6,1.8,"gold",o,0,0.8,0,0.15);
  t.cylinder(0.5,1.2,"dark",o,0.8,1.4,0);
  t.cylinder(0.22,2.8,"orange",o,-0.9,0.9,0.8);
  t.ball(0.25,0.25,0.25,"cream",o,0,1.7,0);
}
,"cartello-divieto-balneazione"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(0.09,2.8,"rope",o,0,1.4,0);
  t.box(2.6,1.8,0.12,"cream",o,0,2.8,0,0.06);
  t.ball(0.65,0.65,0.16,"orange",o,0,2.8,0.08);
  t.ball(0.48,0.48,0.18,"cream",o,0,2.8,0.09);
  t.box(1.0,0.16,0.20,"orange",o,0,2.8,0.1);
}
,"boa-filtrante"(t,e,n){
  const o=oo(e,n,3.5);
  t.cylinder(1.1,1.8,"orange",o,0,0.9,0);
  t.ball(1.15,0.6,1.15,"cream",o,0,1.8,0);
  t.cylinder(0.12,1.6,"dark",o,0,2.6,0);
  t.ball(0.35,0.35,0.35,"gold",o,0,3.4,0);
}
,"tubo-scarico-mare"(t,e,n){
  const o=oo(e,n,4.0);
  t.cylinder(1.4,4.2,"dark",o,0,1.4,0);
  t.cylinder(1.1,4.3,"moss",o,0,1.4,0.1);
  t.ball(1.6,0.8,1.6,"moss",o,0,0.3,1.2);
}
,"ombrellone-spiaggia"(t,e,n){
  const o=oo(e,n,3.8);
  t.cylinder(0.08,3.2,"rope",o,0,1.6,0);
  t.ball(2.2,0.8,2.2,"orange",o,0,3.2,0);
  t.ball(1.8,0.6,1.8,"cream",o,0,3.35,0);
}
,"sdraio-bagnante"(t,e,n){
  const o=oo(e,n,2.0);
  t.box(1.8,0.15,1.2,"rope",o,0,0.4,0);
  t.box(0.12,0.8,1.2,"orange",o,-0.7,0.7,0);
  t.cylinder(0.06,0.7,"rope",o,0.7,0.35,0.5);
  t.cylinder(0.06,0.7,"rope",o,0.7,0.35,-0.5);
}
,"campanello-sos-costa"(t,e,n){
  const o=oo(e,n,3.0);
  t.cylinder(0.1,2.8,"dark",o,0,1.4,0);
  t.box(0.7,1.0,0.5,"orange",o,0,2.2,0,0.08);
  t.ball(0.2,0.2,0.2,"gold",o,0,2.8,0);
}
,"traliccio-tubi"(t,e,n){
  const o=oo(e,n,7.5);
  t.cylinder(0.22,6.5,"dark",o,-3.0,3.25,0);
  t.cylinder(0.22,6.5,"dark",o,3.0,3.25,0);
  t.box(6.8,0.4,1.4,"dark",o,0,5.8,0);
  t.cylinder(0.45,7.0,"cream",o,0,5.0,0.4);
  t.cylinder(0.40,7.0,"orange",o,0,4.2,-0.3);
  t.cylinder(0.35,7.0,"dark",o,0,3.4,0.3);
}
,"fusto-tossico"(t,e,n){
  const o=oo(e,n,1.8);
  t.cylinder(0.52,1.3,"gold",o,0,0.65,0);
  t.cylinder(0.55,0.12,"dark",o,0,1.25,0);
  t.cylinder(0.55,0.12,"dark",o,0,0.05,0);
  t.ball(0.25,0.25,0.06,"dark",o,0,0.65,0.5);
  t.ball(0.9,0.15,0.9,"moss",o,0.4,0.05,0);
}
,"ciminiera-bicolore"(t,e,n){
  const o=oo(e,n,18.0);
  t.cylinder(1.8,4.0,"cream",o,0,2.0,0);
  t.cylinder(1.6,4.0,"orange",o,0,6.0,0);
  t.cylinder(1.4,4.0,"cream",o,0,10.0,0);
  t.cylinder(1.2,4.0,"orange",o,0,14.0,0);
  t.cylinder(1.0,2.5,"dark",o,0,17.2,0);
  t.ball(1.6,1.4,1.6,"dark",o,0,19.2,0);
}
,"manometro-pressione"(t,e,n){
  const o=oo(e,n,1.8);
  t.cylinder(0.12,1.2,"dark",o,0,0.6,0);
  t.cylinder(0.65,0.22,"cream",o,0,1.3,0);
  t.cylinder(0.55,0.25,"gold",o,0,1.3,0.02);
  t.box(0.4,0.06,0.08,"orange",o,0.12,1.35,0.15);
}
,"dirigibile-relique"(t,e,n){
  const o=oo(e,n,15.0);
  t.cylinder(0.35,16.0,"dark",o,0,8.0,0);
  t.cylinder(3.5,0.4,"dark",o,-5.0,8.0,0);
  t.cylinder(4.2,0.4,"dark",o,0,8.0,0);
  t.cylinder(3.5,0.4,"dark",o,5.0,8.0,0);
  t.box(2.5,4.5,0.25,"cream",o,-7.0,8.0,0,0.1);
}
,"cartello-bonifica"(t,e,n){
  const o=oo(e,n,2.8);
  t.cylinder(0.08,2.2,"rope",o,-1.0,1.1,0);
  t.cylinder(0.08,2.2,"rope",o,1.0,1.1,0);
  t.box(2.6,1.4,0.12,"gold",o,0,2.0,0,0.06);
  t.box(2.2,0.25,0.14,"dark",o,0,2.3,0);
  t.box(2.2,0.25,0.14,"dark",o,0,1.7,0);
}
,"pannello-amianto"(t,e,n){
  const o=oo(e,n,3.2);
  t.box(2.8,0.2,2.0,"terrain2",o,0,0.1,0);
  t.box(2.6,0.2,1.8,"terrain",o,0.1,0.3,0.1);
  t.box(2.4,0.2,1.6,"terrain2",o,-0.1,0.5,-0.1);
  t.box(0.8,0.5,0.05,"orange",o,0,0.7,0.8);
}
,"faro-cantiere"(t,e,n){
  const o=oo(e,n,3.5);
  t.cylinder(0.08,3.0,"dark",o,0,1.5,0);
  t.box(0.9,0.6,0.5,"gold",o,-0.4,3.0,0,0.06);
  t.box(0.9,0.6,0.5,"gold",o,0.4,3.0,0,0.06);
  t.ball(0.28,0.28,0.1,"cream",o,-0.4,3.0,0.25);
  t.ball(0.28,0.28,0.1,"cream",o,0.4,3.0,0.25);
}
,"bidone-decontaminazione"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.65,1.6,"cream",o,0,0.8,0);
  t.cylinder(0.70,0.18,"orange",o,0,1.6,0);
  t.box(0.6,0.6,0.06,"orange",o,0,0.8,0.65);
}
,"torre-sveva"(t,e,n){
  const o=oo(e,n,16.0);
  t.cylinder(3.5,12.0,"cream",o,0,6.0,0);
  t.cylinder(4.0,2.0,"cream",o,0,13.0,0);
  t.box(1.2,1.2,0.8,"cream",o,-3.5,14.5,0);
  t.box(1.2,1.2,0.8,"cream",o,3.5,14.5,0);
  t.box(1.2,1.2,0.8,"cream",o,0,14.5,3.5);
  t.box(1.2,1.2,0.8,"cream",o,0,14.5,-3.5);
}
,"stemma-federico"(t,e,n){
  const o=oo(e,n,3.0);
  t.box(2.2,2.8,0.4,"cream",o,0,1.4,0,0.15);
  t.ball(0.8,0.9,0.2,"dark",o,0,1.5,0.22);
  t.box(1.6,0.25,0.25,"gold",o,0,1.5,0.25);
}
,"catapulta-antica"(t,e,n){
  const o=oo(e,n,4.5);
  t.box(3.8,0.6,2.2,"rope",o,0,0.3,0);
  t.cylinder(0.5,0.25,"dark",o,-1.4,0.3,1.1);
  t.cylinder(0.5,0.25,"dark",o,1.4,0.3,1.1);
  t.cylinder(0.5,0.25,"dark",o,-1.4,0.3,-1.1);
  t.cylinder(0.5,0.25,"dark",o,1.4,0.3,-1.1);
  t.cylinder(0.2,3.8,"rope",o,0,2.0,0);
  t.ball(0.6,0.6,0.6,"dark",o,0,3.8,0);
}
,"ponte-levatoio-svevo"(t,e,n){
  const o=oo(e,n,6.5);
  t.box(5.8,0.4,3.2,"rope",o,0,0.2,0);
  t.cylinder(0.12,5.5,"dark",o,-2.4,2.8,1.4);
  t.cylinder(0.12,5.5,"dark",o,2.4,2.8,1.4);
  t.box(0.5,4.8,0.5,"rope",o,-2.6,2.4,-1.4);
  t.box(0.5,4.8,0.5,"rope",o,2.6,2.4,-1.4);
}
,"lanterna-ferro-battuto"(t,e,n){
  const o=oo(e,n,1.8);
  t.cylinder(0.08,0.8,"dark",o,0,0.4,-0.4);
  t.box(0.5,0.8,0.5,"dark",o,0,0.9,0,0.06);
  t.ball(0.22,0.35,0.22,"orange",o,0,0.9,0);
}
,"cannone-antico"(t,e,n){
  const o=oo(e,n,3.2);
  t.box(2.2,0.8,1.4,"rope",o,0,0.4,0);
  t.cylinder(0.42,3.0,"dark",o,0.4,0.7,0);
  t.cylinder(0.45,0.25,"dark",o,-1.0,0.4,0.7);
  t.cylinder(0.45,0.25,"dark",o,-1.0,0.4,-0.7);
}
,"banco-posidonia"(t,e,n){
  const o=oo(e,n,2.8);
  t.ball(1.2,0.4,1.2,"moss",o,0,0.2,0);
  t.cylinder(0.08,1.8,"foliage",o,-0.4,1.0,0.2);
  t.cylinder(0.08,2.0,"foliage",o,0.3,1.1,-0.2);
  t.cylinder(0.08,1.6,"foliage",o,0,0.9,0.3);
  t.ball(0.2,0.8,0.08,"foliage",o,-0.4,1.8,0.2);
  t.ball(0.2,0.9,0.08,"foliage",o,0.3,2.0,-0.2);
}
,"ancora-ammiragliato"(t,e,n){
  const o=oo(e,n,3.8);
  t.cylinder(0.22,3.6,"dark",o,0,1.8,0);
  t.cylinder(0.18,2.4,"dark",o,0,3.2,0);
  t.ball(1.5,0.35,0.35,"dark",o,0,0.4,0);
  t.ball(0.4,0.4,0.15,"gold",o,0,3.6,0);
}
,"falesia-calcarea"(t,e,n){
  const o=oo(e,n,12.0);
  t.box(8.0,10.0,5.0,"cream",o,0,5.0,0,0.35);
  t.box(6.0,8.0,4.0,"terrain2",o,1.0,4.0,-0.5,0.25);
  t.ball(2.5,1.2,2.5,"foliage",o,0,10.2,0);
}
,"campana-nebbia"(t,e,n){
  const o=oo(e,n,2.6);
  t.box(0.8,2.4,0.8,"cream",o,0,1.2,0);
  t.ball(0.55,0.65,0.55,"gold",o,0,2.6,0);
  t.cylinder(0.06,0.6,"dark",o,0,2.2,0);
}
,"gabbiano-scoglio"(t,e,n){
  const o=oo(e,n,1.4);
  t.ball(0.8,0.5,0.8,"cream",o,0,0.25,0);
  t.ball(0.35,0.22,0.18,"cream",o,0,0.6,0);
  t.ball(0.14,0.14,0.14,"cream",o,0.25,0.75,0);
  t.box(0.2,0.05,0.06,"gold",o,0.4,0.75,0);
  t.box(0.08,0.45,0.6,"dark",o,-0.1,0.65,0);
}
,"fenicottero-rosa"(t,e,n){
  const o=oo(e,n,2.8);
  t.cylinder(0.04,1.6,"orangeLight",o,-0.12,0.8,0);
  t.cylinder(0.04,1.6,"orangeLight",o,0.12,0.8,0);
  t.ball(0.45,0.32,0.28,"orangeLight",o,0,1.7,0);
  t.cylinder(0.06,1.2,"orangeLight",o,0.22,2.2,0);
  t.ball(0.18,0.15,0.14,"orangeLight",o,0.25,2.8,0);
  t.box(0.22,0.07,0.07,"dark",o,0.36,2.78,0);
}
,"paratoia-salina"(t,e,n){
  const o=oo(e,n,3.8);
  t.box(0.4,3.2,0.4,"rope",o,-1.4,1.6,0);
  t.box(0.4,3.2,0.4,"rope",o,1.4,1.6,0);
  t.box(2.6,2.0,0.18,"rope",o,0,1.2,0);
  t.cylinder(0.35,0.12,"gold",o,0,2.8,0);
}
,"badile-salinaio"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.05,2.2,"rope",o,0,1.1,0);
  t.box(0.65,0.8,0.08,"rope",o,0,0.4,0);
}
,"carrello-sale"(t,e,n){
  const o=oo(e,n,3.0);
  t.box(2.4,1.2,1.6,"rope",o,0,0.8,0);
  t.cylinder(0.35,0.18,"dark",o,-0.8,0.35,0.85);
  t.cylinder(0.35,0.18,"dark",o,0.8,0.35,0.85);
  t.cylinder(0.35,0.18,"dark",o,-0.8,0.35,-0.85);
  t.cylinder(0.35,0.18,"dark",o,0.8,0.35,-0.85);
  t.ball(0.9,0.5,0.7,"cream",o,0,1.4,0);
}
,"cannone-borbonico"(t,e,n){
  const o=oo(e,n,3.5);
  t.box(2.4,0.9,1.5,"rope",o,0,0.5,0);
  t.cylinder(0.45,3.4,"gold",o,0.3,0.8,0);
  t.cylinder(0.55,0.22,"dark",o,-0.8,0.5,0.8);
  t.cylinder(0.55,0.22,"dark",o,0.8,0.5,0.8);
  t.cylinder(0.55,0.22,"dark",o,-0.8,0.5,-0.8);
  t.cylinder(0.55,0.22,"dark",o,0.8,0.5,-0.8);
}
,"garitta-vedetta"(t,e,n){
  const o=oo(e,n,5.0);
  t.cylinder(1.4,4.2,"cream",o,0,2.1,0);
  t.ball(1.5,0.9,1.5,"cream",o,0,4.4,0);
  t.box(0.8,2.0,0.3,"dark",o,0,1.5,1.3);
}
,"piramide-palle-cannone"(t,e,n){
  const o=oo(e,n,1.8);
  t.ball(0.3,0.3,0.3,"dark",o,-0.3,0.3,-0.3);
  t.ball(0.3,0.3,0.3,"dark",o,0.3,0.3,-0.3);
  t.ball(0.3,0.3,0.3,"dark",o,-0.3,0.3,0.3);
  t.ball(0.3,0.3,0.3,"dark",o,0.3,0.3,0.3);
  t.ball(0.3,0.3,0.3,"dark",o,0,0.8,0);
}
,"argano-catena-porto"(t,e,n){
  const o=oo(e,n,3.0);
  t.box(1.8,1.4,1.4,"dark",o,0,0.7,0);
  t.cylinder(0.5,1.2,"rope",o,0,1.0,0);
  t.cylinder(0.8,0.15,"gold",o,0.9,1.0,0);
}
,"bandiera-sicilia"(t,e,n){
  const o=oo(e,n,5.5);
  t.cylinder(0.08,5.2,"gold",o,0,2.6,0);
  t.box(2.2,1.4,0.06,"orange",o,1.1,4.4,0);
  t.ball(0.3,0.3,0.08,"gold",o,1.1,4.4,0.04);
}
,"vaso-caltagirone"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(0.7,1.8,"cream",o,0,0.9,0);
  t.cylinder(0.9,0.3,"gold",o,0,1.8,0);
  t.ball(1.2,1.0,1.2,"orange",o,0,2.4,0);
  t.ball(0.8,0.8,0.8,"foliage",o,0,2.8,0);
}
,"ficus-rinascita"(t,e,n){
  const o=oo(e,n,14.0);
  t.cylinder(2.2,5.5,"rope",o,0,2.75,0);
  t.cylinder(0.9,5.0,"rope",o,-1.8,2.5,0.9);
  t.cylinder(0.8,5.2,"rope",o,1.7,2.6,-0.8);
  t.ball(5.8,2.6,5.8,"foliage",o,0,7.2,0);
  t.ball(4.2,2.2,4.2,"moss",o,-3.2,7.8,1.5);
  t.ball(4.4,2.3,4.4,"foliage",o,3.0,7.6,-1.4);
  t.ball(0.4,0.4,0.4,"orange",o,1.2,7.4,1.8);
  t.ball(0.4,0.4,0.4,"orange",o,-1.4,7.8,-1.5);
  t.ball(0.4,0.4,0.4,"orange",o,2.2,8.0,-0.8);
}
,"palina-raccolta-differenziata"(t,e,n){
  const o=oo(e,n,2.2);
  t.box(0.5,1.4,0.5,"foliage",o,-0.9,0.7,0);
  t.box(0.5,1.4,0.5,"gold",o,-0.3,0.7,0);
  t.box(0.5,1.4,0.5,"cream",o,0.3,0.7,0);
  t.box(0.5,1.4,0.5,"orange",o,0.9,0.7,0);
}
,"arco-trionfale-verde"(t,e,n){
  const o=oo(e,n,9.0);
  t.cylinder(0.6,7.0,"foliage",o,-3.5,3.5,0);
  t.cylinder(0.6,7.0,"foliage",o,3.5,3.5,0);
  t.box(8.2,1.2,1.2,"foliage",o,0,7.2,0,0.2);
  t.ball(0.8,0.8,0.8,"orange",o,0,8.2,0);
  t.ball(0.5,0.5,0.5,"gold",o,-2.5,7.8,0);
  t.ball(0.5,0.5,0.5,"gold",o,2.5,7.8,0);
}
,"scarico-fogna-liquami"(t,e,n){
  const o=oo(e,n,4.5);
  // Cracked concrete sewer culvert pipe
  t.cylinder(1.6,3.6,"dark",o,0,1.8,0);
  t.cylinder(1.85,0.5,"orange",o,0,3.3,0);
  // Overflowing toxic brown/black sewage torrent
  t.box(2.6,5.2,1.5,"dark",o,0,-1.0,0,0.2);
  // Foamy toxic bubbles and sludge clumps
  t.ball(0.85,0.45,0.85,"gold",o,-0.5,-1.2,0.6);
  t.ball(0.75,0.40,0.75,"cream",o,0.6,-1.6,0.5);
  t.ball(0.95,0.50,0.95,"dark",o,0.1,-2.2,0.4);
}
,"ciminiera-fumo-animata"(t,e,n){
  const o=oo(e,n,20.0);
  // Alternating red and white warning bands of the refinery stack
  t.cylinder(1.35,4.0,"orange",o,0,2.0,0);
  t.cylinder(1.30,4.0,"cream",o,0,6.0,0);
  t.cylinder(1.25,4.0,"orange",o,0,10.0,0);
  t.cylinder(1.20,4.0,"cream",o,0,14.0,0);
  t.cylinder(1.15,4.0,"orange",o,0,18.0,0);
  t.cylinder(1.50,0.6,"dark",o,0,20.2,0);
  // Billowing petrochemical smog clouds puffing into the sky
  t.ball(2.4,1.8,2.4,"dark",o,0.8,22.0,0);
  t.ball(2.8,2.2,2.8,"cream",o,2.2,24.2,0.5);
  t.ball(3.2,2.5,3.2,"dark",o,3.8,27.0,1.0);
}
,"discarica-abusiva"(t,e,n){
  const o=oo(e,n,6.0);
  // Mound of illegal waste and compressed refuse
  t.box(7.5,2.4,4.2,"dark",o,0,1.2,0,0.3);
  // Piled garbage bags (black/dark plastic)
  t.ball(1.4,1.1,1.4,"dark",o,-1.8,2.2,0.5);
  t.ball(1.3,1.0,1.3,"dark",o,1.6,2.1,-0.6);
  t.ball(1.5,1.2,1.5,"orange",o,0.1,2.6,0.2);
  // Discarded truck tires
  t.cylinder(0.95,0.6,"dark",o,-2.4,1.2,1.2);
  t.cylinder(0.95,0.6,"dark",o,2.2,1.0,1.0);
  // Leaning corrugated rusty sheets
  t.box(3.2,1.8,0.25,"rope",o,-0.5,1.8,-1.2,0.1);
  // Toxic yellow chemical container
  t.cylinder(0.4,1.0,"gold",o,1.0,1.6,1.4);
}
,"liquame-tossico-pozza"(t,e,n){
  const o=oo(e,n,4.0);
  // Sprawling toxic petrochemical puddle with sludge
  t.cylinder(3.6,0.22,"dark",o,0,0.11,0);
  t.ball(2.2,0.14,2.2,"gold",o,-0.6,0.18,0.4);
  t.ball(1.6,0.12,1.6,"orange",o,0.8,0.19,-0.5);
  // Corroded warning sign post
  t.cylinder(0.08,2.8,"rope",o,-1.6,1.4,0);
  t.box(1.4,1.4,0.1,"orange",o,-1.6,2.6,0,0.05);
  t.ball(0.3,0.3,0.12,"cream",o,-1.6,2.6,0.06);
}
,"fusto-tossico-sversato"(t,e,n){
  const o=oo(e,n,3.0);
  // Crushed chemical drum on its side
  t.cylinder(0.7,1.8,"orange",o,0,0.6,0);
  t.cylinder(0.72,0.15,"dark",o,0,0.6,0.6);
  t.cylinder(0.72,0.15,"dark",o,0,0.6,-0.6);
  // Spilled pool of toxic chemical sludge
  t.box(3.0,0.16,2.2,"gold",o,1.2,0.08,0,0.1);
  t.ball(0.4,0.35,0.4,"gold",o,1.8,0.25,0.3);
  t.ball(0.35,0.30,0.35,"gold",o,2.2,0.22,-0.4);
}
,"fumo-petrolchimico-nube"(t,e,n){
  const o=oo(e,n,14.0);
  // Giant heavy petrochemical smog cloud in the background sky
  t.ball(7.2,3.2,5.0,"dark",o,0,3.2,0);
  t.ball(5.4,2.8,4.2,"cream",o,-3.5,3.6,0.8);
  t.ball(5.6,2.9,4.4,"dark",o,3.6,3.8,-0.6);
}
,"torcia-petrolchimico-fiamma"(t,e,n){
  const o=oo(e,n,22.0);
  // Tall industrial refinery flare stack mast
  t.cylinder(0.45,22.0,"dark",o,0,11.0,0);
  t.box(1.8,1.8,0.4,"orange",o,0,14.0,0);
  t.box(1.6,1.6,0.4,"orange",o,0,18.0,0);
  t.cylinder(0.9,1.4,"dark",o,0,22.5,0);
  // Roaring flare flame
  t.ball(1.6,3.4,1.6,"orange",o,0,24.8,0);
  t.ball(1.1,2.4,1.1,"gold",o,0,25.2,0);
  // Carbon soot cloud
  t.ball(2.6,1.8,2.6,"dark",o,0.8,27.4,0);
}
,"rifiuti-plastica-costa"(t,e,n){
  const o=oo(e,n,4.2);
  // Washed-up marine trash, styrofoam and tangled nets
  t.box(4.2,1.2,2.4,"cream",o,0,0.6,0,0.15);
  t.ball(0.8,0.8,0.8,"orange",o,-1.2,1.2,0.4);
  t.ball(0.7,0.7,0.7,"rope",o,1.1,1.1,-0.5);
  t.cylinder(0.3,1.2,"dark",o,0.2,1.0,0.6);
}
,"cato-carrucola-acqua"(t,e,n){
  const o=oo(e,n,7.5);
  // Sturdy vertical wooden timber post
  t.cylinder(0.24,6.2,"rope",o,0,3.1,0);
  // Heavy timber base support blocks
  t.box(1.2,0.5,1.2,"rope",o,0,0.25,0);
  // Horizontal cantilever beam reaching over
  t.box(3.2,0.32,0.32,"rope",o,1.2,5.9,0);
  // Diagonal brace strut
  t.box(1.8,0.22,0.22,"rope",o,0.7,5.0,0,-0.78);
  // Iron pulley housing & grooved wheel
  t.cylinder(0.40,0.18,"dark",o,2.4,5.7,0);
  t.cylinder(0.48,0.06,"gold",o,2.4,5.7,0);
  // Hanging hemp rope with wooden pull handle at player reach height
  t.cylinder(0.04,4.2,"rope",o,1.6,3.6,0);
  t.ball(0.25,0.25,0.25,"orange",o,1.6,1.5,0);
  t.cylinder(0.12,0.28,"gold",o,1.6,1.4,0);
  // The 'Cato' (Wooden Water Bucket) suspended from the pulley
  t.cylinder(0.68,1.2,"orange",o,2.4,4.4,0);
  t.cylinder(0.72,0.12,"dark",o,2.4,4.8,0);
  t.cylinder(0.70,0.12,"dark",o,2.4,4.0,0);
  // Surface of pure blue water inside the cato
  t.cylinder(0.62,0.08,"cream",o,2.4,4.9,0);
  t.ball(0.2,0.2,0.2,"cream",o,2.3,5.0,0.1);
}
,"ficus-chioma-attraversabile"(t,e,n){
  const o=oo(e,n,14.0);
  // Giant multi-pillar gnarled ficus trunk
  t.cylinder(1.4,11.5,"bark",o,0,5.75,0);
  // Characteristic aerial roots hanging down into the spike pit
  t.cylinder(0.24,11.2,"vine",o,-3.2,5.6,0.5);
  t.cylinder(0.22,10.8,"vine",o,3.4,5.4,-0.4);
  t.cylinder(0.26,10.5,"vine",o,-1.6,5.25,-0.6);
  t.cylinder(0.22,11.0,"vine",o,1.7,5.5,0.5);
  t.cylinder(0.18,9.5,"vine",o,-4.8,4.75,0.2);
  t.cylinder(0.18,9.5,"vine",o,4.9,4.75,-0.2);
  // Massive undulating walkable green canopy (chioma di ficus)
  t.ball(7.2,2.0,3.6,"foliage",o,0,11.4,0);
  t.ball(4.8,1.8,3.2,"cityHerb",o,-4.2,11.2,0.2);
  t.ball(5.0,1.9,3.4,"cityHerb",o,4.2,11.2,-0.2);
  t.ball(4.4,1.6,2.8,"foliage",o,-1.6,11.0,0.8);
  t.ball(4.4,1.6,2.8,"cityHerb",o,1.6,11.0,-0.8);
  // Ripening golden figs / gemme di ficus
  t.ball(0.25,0.25,0.25,"gold",o,-2.2,12.0,1.2);
  t.ball(0.25,0.25,0.25,"gold",o,2.4,12.1,1.1);
  t.ball(0.25,0.25,0.25,"gold",o,0.4,12.3,-1.2);
}
,"ficus-germoglio-irrigato"(t,e,n){
  const o=oo(e,n,3.2);
  // Clay terracotta pot
  t.cylinder(0.65,0.8,"orange",o,0,0.4,0);
  t.cylinder(0.72,0.18,"orange",o,0,0.75,0);
  // Dry earth
  t.cylinder(0.60,0.1,"dark",o,0,0.72,0);
  // Young ficus stem and spreading roots
  t.cylinder(0.10,1.4,"rope",o,0,1.3,0);
  // Sprouting green leaves
  t.ball(0.45,0.25,0.35,"gold",o,0,1.9,0);
  t.ball(0.35,0.20,0.28,"orange",o,-0.3,1.7,0.2);
  t.ball(0.35,0.20,0.28,"orange",o,0.3,1.6,-0.2);
}
'''

