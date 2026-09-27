# tools/gta_decor_models.py
"""
Complete Procedural 3D Clay Models for GTA Giuseppe Taglia Alberi:
- 12 Lush Trees & Plants (Ficus secolari, Mediterranean palms, orange/citrus trees, olive trees, saplings)
  All proportioned for optimal camera framing with rich bark and vibrant layered foliage.
- Historical Augusta Architecture & Cultural monuments
- Environmental hazards & ecological elements
"""

def get_all_augusta_decor_models():
    return '''
,"ficus-centenario"(t,e,n){
  const o=oo(e,n,10.0);
  // Monumental Ficus macrophylla of Villa Comunale di Augusta (1850)
  // Main ancient fluted trunk with rich dark bark
  t.cylinder(1.8,3.8,"bark",o,0,1.9,0);
  // 4 massive buttress pillar roots anchoring into soil
  t.cylinder(0.75,3.4,"bark",o,-1.4,1.7,0.7);
  t.cylinder(0.70,3.5,"bark",o,1.3,1.75,-0.6);
  t.cylinder(0.60,3.2,"bark",o,0.7,1.6,1.2);
  t.cylinder(0.65,3.3,"bark",o,-1.2,1.65,-1.1);
  // Spreading root flare base
  t.ball(2.6,0.6,2.6,"bark",o,0,0.3,0);
  // Hanging aerial roots descending like pillars
  t.cylinder(0.10,3.0,"bark",o,-2.4,3.0,0.9);
  t.cylinder(0.09,2.8,"bark",o,2.2,2.9,-0.9);
  t.cylinder(0.11,3.2,"bark",o,-0.9,3.1,2.0);
  t.cylinder(0.08,2.9,"bark",o,1.8,2.9,1.6);
  // Sprawling massive emerald green clay canopy (perfect camera height: y=4.5 to 7.0)
  t.ball(4.8,2.2,4.4,"foliage",o,0,4.8,0);
  t.ball(3.6,1.8,3.4,"foliage",o,-2.6,5.2,1.0);
  t.ball(3.8,1.9,3.5,"foliage",o,2.4,5.0,-0.9);
  t.ball(3.0,1.6,3.0,"leafLight",o,0.6,5.8,1.5);
  t.ball(3.2,1.7,3.1,"leafLight",o,-1.2,5.6,-1.8);
  t.ball(2.6,1.4,2.5,"leafLight",o,0,6.5,0.3);
  // Drooping leafy branches that arch right over Giuseppe
  t.ball(1.6,1.0,1.6,"foliage",o,-3.5,3.8,0.5);
  t.ball(1.6,1.0,1.6,"leafLight",o,3.2,3.7,-0.5);
  t.ball(1.8,1.1,1.8,"foliage",o,0,3.6,2.4);
}
,"secular-ficus"(t,e,n){
  _D["ficus-centenario"](t,e,n);
}
,"palma-augusta"(t,e,n){
  const o=oo(e,n,7.5);
  // Root flare base anchored into Sicilian soil
  t.ball(1.4,0.4,1.4,"bark",o,0,0.2,0);
  t.cylinder(0.7,0.35,"bark",o,0,0.18,0);
  // Curved ringed Mediterranean date palm trunk
  t.cylinder(0.42,4.5,"bark",o,0,2.25,0);
  for(let r=1;r<6;r++){
    t.cylinder(0.49,0.12,"dark",o,0,r*0.8,0);
  }
  // Drooping fan fronds canopy radiating at y=4.5 to 5.5
  t.ball(2.4,0.5,2.4,"foliage",o,0,4.6,0);
  t.ball(3.2,0.35,1.2,"foliage",o,1.2,4.4,0);
  t.ball(3.2,0.35,1.2,"foliage",o,-1.2,4.4,0);
  t.ball(1.2,0.35,3.2,"foliage",o,0,4.4,1.2);
  t.ball(1.2,0.35,3.2,"foliage",o,0,4.4,-1.2);
  t.ball(2.4,0.4,2.4,"leafLight",o,0,5.0,0);
  // Cascading palm fronds tips dipping down
  t.ball(1.2,0.4,0.8,"leafLight",o,2.4,3.8,0);
  t.ball(1.2,0.4,0.8,"leafLight",o,-2.4,3.8,0);
  t.ball(0.8,0.4,1.2,"leafLight",o,0,3.8,2.4);
  t.ball(0.8,0.4,1.2,"leafLight",o,0,3.8,-2.4);
  // Golden date clusters
  t.ball(0.45,0.6,0.45,"gold",o,0.35,4.0,0.25);
  t.ball(0.40,0.55,0.40,"gold",o,-0.35,4.0,-0.25);
}
,"palma-dattilifera"(t,e,n){
  _D["palma-augusta"](t,e,n);
}
,"arancio-siciliano"(t,e,n){
  const o=oo(e,n,5.5);
  // Root flare base anchored into Sicilian soil
  t.ball(1.1,0.35,1.1,"bark",o,0,0.18,0);
  t.cylinder(0.55,0.3,"bark",o,0,0.15,0);
  // Sicilian citrus / orange tree
  t.cylinder(0.35,2.6,"bark",o,0,1.3,0);
  t.cylinder(0.22,1.6,"bark",o,0.4,2.2,0.25);
  t.cylinder(0.20,1.5,"bark",o,-0.4,2.1,-0.2);
  // Lush round green canopy at eye level
  t.ball(2.2,1.7,2.2,"foliage",o,0,3.4,0);
  t.ball(1.6,1.3,1.6,"leafLight",o,-0.7,3.6,0.4);
  t.ball(1.5,1.2,1.5,"foliage",o,0.7,3.5,-0.3);
  t.ball(1.3,1.1,1.3,"leafLight",o,0,4.2,0);
  // Bright orange clay fruits hanging prominently
  t.ball(0.22,0.22,0.22,"orange",o,0.7,2.8,1.2);
  t.ball(0.22,0.22,0.22,"orange",o,-0.9,3.0,0.7);
  t.ball(0.22,0.22,0.22,"orange",o,1.0,3.3,-0.6);
  t.ball(0.22,0.22,0.22,"orange",o,-0.4,3.7,-1.1);
  t.ball(0.22,0.22,0.22,"orange",o,0.3,4.0,0.9);
  t.ball(0.22,0.22,0.22,"orange",o,-0.7,3.4,-0.6);
  t.ball(0.20,0.20,0.20,"orange",o,0.1,2.9,-1.2);
}
,"olivo-secolare"(t,e,n){
  const o=oo(e,n,5.8);
  // Gnarled root flare base anchored into rocky soil
  t.ball(1.6,0.5,1.6,"bark",o,0,0.25,0);
  t.cylinder(0.9,0.4,"bark",o,0,0.2,0);
  // Ancient gnarled Sicilian olive tree
  t.cylinder(0.58,2.4,"bark",o,0,1.2,0);
  t.cylinder(0.38,1.8,"bark",o,-0.35,2.1,0.25);
  t.cylinder(0.36,1.8,"bark",o,0.4,2.2,-0.2);
  t.cylinder(0.16,1.2,"dark",o,0.15,1.3,0.4);
  // Silvery-green olive foliage
  t.ball(2.4,1.2,2.0,"foliage",o,0,3.2,0);
  t.ball(1.8,1.0,1.6,"leafLight",o,-1.0,3.4,0.3);
  t.ball(1.9,1.1,1.7,"leafLight",o,1.0,3.3,-0.25);
  t.ball(1.4,0.9,1.3,"foliage",o,0,3.9,0);
  // Dark ripe olives
  t.ball(0.12,0.15,0.12,"dark",o,0.8,2.7,0.7);
  t.ball(0.12,0.15,0.12,"dark",o,-0.7,2.8,-0.6);
  t.ball(0.12,0.15,0.12,"dark",o,-0.3,2.6,0.9);
}
,"tree-sapling"(t,e,n){
  const o=oo(e,n,3.5);
  // Young replanted tree with protective wooden stakes
  t.ball(1.1,0.25,1.1,"bark",o,0,0.12,0);
  t.cylinder(0.09,2.6,"bark",o,0,1.3,0);
  // Wooden stakes
  t.cylinder(0.05,2.4,"bark",o,-0.35,1.2,0);
  t.cylinder(0.05,2.4,"bark",o,0.35,1.2,0);
  // Crossbar & ties
  t.box(0.8,0.05,0.05,"dark",o,0,1.5,0);
  t.cylinder(0.12,0.06,"dark",o,-0.35,1.5,0);
  t.cylinder(0.12,0.06,"dark",o,0.35,1.5,0);
  // Fresh young vibrant leaves
  t.ball(0.9,0.8,0.9,"leafLight",o,0,2.8,0);
  t.ball(0.7,0.6,0.7,"foliage",o,-0.25,3.0,0.15);
  t.ball(0.7,0.6,0.7,"leafLight",o,0.25,3.1,-0.15);
  t.ball(0.45,0.5,0.45,"foliage",o,0,3.5,0);
}
,"alberello-rinascita"(t,e,n){
  _D["tree-sapling"](t,e,n);
}
,"ficus-rinascita"(t,e,n){
  const o=oo(e,n,4.5);
  // Soil mound & stone border
  t.ball(1.6,0.35,1.6,"bark",o,0,0.18,0);
  for(let a=0;a<6;a++){
    const ang=a*Math.PI/3;
    t.box(0.45,0.22,0.35,"cream",o,Math.cos(ang)*1.1,0.18,Math.sin(ang)*1.1,0.1);
  }
  // Vigorously sprouting ficus
  t.cylinder(0.25,2.6,"bark",o,0,1.3,0);
  t.cylinder(0.09,1.8,"bark",o,-0.5,1.2,0.35);
  t.cylinder(0.09,1.8,"bark",o,0.5,1.3,-0.35);
  // Layered green canopy
  t.ball(1.9,1.3,1.9,"foliage",o,0,3.1,0);
  t.ball(1.4,1.1,1.4,"leafLight",o,-0.7,3.4,0.5);
  t.ball(1.5,1.2,1.5,"leafLight",o,0.7,3.5,-0.4);
  t.ball(1.0,0.8,1.0,"foliage",o,0,4.1,0);
  // Golden blossoms
  t.ball(0.22,0.22,0.22,"gold",o,0.6,2.9,0.7);
  t.ball(0.22,0.22,0.22,"gold",o,-0.6,3.0,-0.6);
  t.ball(0.25,0.25,0.25,"gold",o,0,4.2,0.2);
}
,"ficus-chioma-attraversabile"(t,e,n){
  const o=oo(e,n,9.0);
  // Sprawling walkable canopy for the water contraption
  t.cylinder(1.1,4.2,"bark",o,0,2.1,0);
  t.cylinder(0.45,3.4,"bark",o,-1.8,2.7,0.7);
  t.cylinder(0.45,3.4,"bark",o,1.8,2.7,-0.7);
  // Wide thick horizontal green canopy pad
  t.box(9.0,1.2,3.8,"foliage",o,0,4.8,0,0.35);
  t.ball(4.2,1.4,3.2,"leafLight",o,-1.6,5.1,0);
  t.ball(4.2,1.4,3.2,"leafLight",o,1.6,5.1,0);
  t.ball(2.6,1.0,2.2,"foliage",o,0,5.5,0);
  // Hanging leafy vines
  t.cylinder(0.07,2.2,"foliage",o,-3.0,3.8,1.0);
  t.cylinder(0.07,2.4,"foliage",o,3.0,3.8,-1.0);
  t.ball(0.3,0.3,0.3,"gold",o,0,5.7,0.4);
}
,"ficus-germoglio-irrigato"(t,e,n){
  const o=oo(e,n,3.0);
  // Freshly irrigated sprout with water droplets
  t.ball(1.2,0.25,1.2,"bark",o,0,0.12,0);
  t.cylinder(0.16,1.8,"bark",o,0,0.9,0);
  t.ball(1.0,0.8,1.0,"foliage",o,0,2.1,0);
  t.ball(0.8,0.7,0.8,"leafLight",o,-0.35,2.3,0.25);
  t.ball(0.8,0.7,0.8,"leafLight",o,0.35,2.3,-0.25);
  // Sparkling water drops
  t.ball(0.18,0.22,0.18,"blueLight",o,0.4,2.0,0.5);
  t.ball(0.18,0.22,0.18,"blueLight",o,-0.4,2.1,-0.4);
  t.ball(0.20,0.24,0.20,"blueLight",o,0,2.6,0);
}
,"cato-carrucola-acqua"(t,e,n){
  const o=oo(e,n,4.5);
  // Wooden A-frame scaffold
  t.cylinder(0.12,4.8,"bark",o,-1.4,2.4,-0.6);
  t.cylinder(0.12,4.8,"bark",o,-1.4,2.4,0.6);
  t.cylinder(0.12,4.8,"bark",o,1.4,2.4,-0.6);
  t.cylinder(0.12,4.8,"bark",o,1.4,2.4,0.6);
  // Top crossbeam
  t.box(3.4,0.2,0.2,"bark",o,0,4.7,0);
  // Pulley wheel
  t.cylinder(0.45,0.12,"dark",o,0,4.4,0);
  t.ball(0.18,0.18,0.18,"gold",o,0,4.4,0);
  // Rope
  t.cylinder(0.04,2.2,"rope",o,0,3.2,0);
  // Bucket
  t.cylinder(0.65,0.9,"bark",o,0,1.9,0);
  t.cylinder(0.70,0.1,"dark",o,0,2.2,0);
  t.cylinder(0.66,0.1,"dark",o,0,1.6,0);
  t.cylinder(0.62,0.15,"blueLight",o,0,2.3,0);
}
,"barocco-duomo"(t,e,n){
  const o=oo(e,n,18.0);
  // Chiesa Madre di Augusta (Santa Maria Assunta in Cielo, 1693-1769)
  // Ground Floor (First Order) - warm Sicilian limestone
  t.box(14.0,1.2,3.0,"cream",o,0,0.6,0);
  t.box(15.0,0.4,3.6,"cream",o,0,0.2,0.2); // steps
  t.box(12.5,7.5,2.4,"cream",o,0,4.95,0);
  // 4 Corinthian pilasters
  t.cylinder(0.45,7.6,"cream",o,-5.2,5.0,1.25);
  t.cylinder(0.45,7.6,"cream",o,-2.4,5.0,1.25);
  t.cylinder(0.45,7.6,"cream",o,2.4,5.0,1.25);
  t.cylinder(0.45,7.6,"cream",o,5.2,5.0,1.25);
  // Column capitals
  t.box(1.2,0.6,1.2,"gold",o,-5.2,8.9,1.25);
  t.box(1.2,0.6,1.2,"gold",o,-2.4,8.9,1.25);
  t.box(1.2,0.6,1.2,"gold",o,2.4,8.9,1.25);
  t.box(1.2,0.6,1.2,"gold",o,5.2,8.9,1.25);
  // Central Main Portal: arched recessed entrance & broken pediment
  t.box(2.8,5.2,1.2,"dark",o,0,3.8,0.8);
  t.cylinder(1.4,1.2,"dark",o,0,6.4,0.8);
  t.box(3.4,0.4,0.6,"gold",o,0,7.4,1.3);
  // Side niches with carved statues
  t.box(1.4,3.2,0.6,"dark",o,-3.8,4.5,1.15);
  t.box(1.4,3.2,0.6,"dark",o,3.8,4.5,1.15);
  t.cylinder(0.3,1.8,"cream",o,-3.8,4.2,1.2);
  t.cylinder(0.3,1.8,"cream",o,3.8,4.2,1.2);
  // Intermediate entablature separating orders
  t.box(13.6,1.0,2.8,"cream",o,0,9.2,0);
  t.box(14.2,0.4,3.0,"gold",o,0,9.7,0);
  // Second Order (Upper tier)
  t.box(8.2,6.0,2.2,"cream",o,0,12.7,-0.1);
  // Baroque S-curved scroll volutes (ampie volute a ricciolo)
  t.cylinder(1.8,2.0,"cream",o,-5.2,11.2,0.8);
  t.cylinder(1.8,2.0,"cream",o,5.2,11.2,0.8);
  t.ball(1.2,1.2,1.2,"gold",o,-5.8,12.6,0.9);
  t.ball(1.2,1.2,1.2,"gold",o,5.8,12.6,0.9);
  // Upper pilasters
  t.cylinder(0.4,5.8,"cream",o,-2.8,12.6,1.05);
  t.cylinder(0.4,5.8,"cream",o,2.8,12.6,1.05);
  // Central Baroque upper window with pediment
  t.box(2.2,3.6,0.8,"dark",o,0,12.8,1.0);
  t.cylinder(1.1,0.8,"dark",o,0,14.6,1.0);
  t.box(2.8,0.4,0.6,"gold",o,0,15.3,1.1);
  // Top Entablature & Bell Gable (Cella campanaria)
  t.box(9.2,0.8,2.4,"cream",o,0,16.1,-0.1);
  t.box(5.4,3.4,1.8,"cream",o,0,18.2,-0.2);
  // Belfry arched openings
  t.box(1.2,2.0,1.9,"dark",o,-1.3,18.0,-0.2);
  t.box(1.2,2.0,1.9,"dark",o,1.3,18.0,-0.2);
  // Bronze bells
  t.cylinder(0.35,0.8,"gold",o,-1.3,18.2,-0.2);
  t.cylinder(0.35,0.8,"gold",o,1.3,18.2,-0.2);
  // Triangular pediment
  t.box(6.0,0.6,2.0,"cream",o,0,20.2,-0.2);
  // Elevated Latin Stone Cross at top summit
  t.box(0.3,2.4,0.3,"gold",o,0,21.6,-0.2);
  t.box(1.6,0.3,0.3,"gold",o,0,22.1,-0.2);
}
,"duomo-facade"(t,e,n){
  _D["barocco-duomo"](t,e,n);
}
,"porta-spagnola"(t,e,n){
  const o=oo(e,n,10.0);
  t.box(2.0,7.0,2.2,"cream",o,-3.5,3.5,0,0.15);
  t.box(2.0,7.0,2.2,"cream",o,3.5,3.5,0,0.15);
  t.box(5.8,1.5,2.0,"cream",o,0,6.6,0,0.15);
  t.box(3.0,1.2,1.2,"gold",o,0,8.0,0);
  t.cylinder(0.3,2.4,"dark",o,0,4.2,0);
  t.cylinder(0.3,2.4,"dark",o,-1.2,4.2,0);
  t.cylinder(0.3,2.4,"dark",o,1.2,4.2,0);
}
,"bastione-spagnolo"(t,e,n){
  const o=oo(e,n,9.0);
  t.box(9.0,5.5,4.0,"cream",o,0,2.75,0,0.2);
  t.box(10.0,0.8,4.6,"dark",o,0,5.6,0);
  for(let c=-3;c<=3;c+=2){
    t.box(1.2,1.2,1.2,"cream",o,c,6.4,1.8,0.1);
  }
}
,"hangar-arch"(t,e,n){
  const o=oo(e,n,14.0);
  t.box(1.2,7.5,1.6,"cream",o,-6,3.75,0,0.15);
  t.box(1.2,7.5,1.6,"cream",o,6,3.75,0,0.15);
  t.box(1.0,6,1.4,"cream",o,-4.2,9.5,0,0.15);
  t.box(1.0,6,1.4,"cream",o,4.2,9.5,0,0.15);
  t.box(7.5,0.9,1.4,"cream",o,0,12.2,0,0.15);
  t.box(13.0,0.3,1.8,"dark",o,0,12.8,0);
}
,"salt-windmill"(t,e,n){
  const o=oo(e,n,5.5);
  t.cylinder(1.3,4.2,"cream",o,0,2.1,0);
  t.cylinder(1.5,1.1,"bark",o,0,4.8,0);
  t.ball(0.45,0.45,0.45,"dark",o,0,4.4,1.4);
  t.box(0.22,4.4,0.08,"bark",o,0,4.4,1.45);
  t.box(4.4,0.22,0.08,"bark",o,0,4.4,1.45);
}
,"salt-pyramid"(t,e,n){
  const o=oo(e,n,4.0);
  t.box(5.5,1.1,4.2,"cream",o,0,0.55,0,0.2);
  t.box(3.8,1.1,2.9,"cream",o,0,1.65,0,0.2);
  t.ball(1.5,1.2,1.3,"cream",o,0,2.6,0);
}
,"lighthouse-tower"(t,e,n){
  const o=oo(e,n,9.5);
  t.cylinder(1.7,3.0,"cream",o,0,1.5,0);
  t.cylinder(1.5,2.0,"dark",o,0,4.0,0);
  t.cylinder(1.3,2.8,"cream",o,0,6.4,0);
  t.cylinder(1.8,0.3,"dark",o,0,8.0,0);
  t.cylinder(1.0,1.2,"gold",o,0,8.8,0);
  t.cylinder(1.2,0.6,"dark",o,0,9.7,0);
}
,"oil-tank"(t,e,n){
  const o=oo(e,n,5.0);
  t.cylinder(2.2,3.6,"dark",o,0,1.8,0);
  t.ball(2.2,0.7,2.2,"orange",o,0,3.6,0);
  t.cylinder(2.35,0.14,"orangeLight",o,0,1.2,0);
  t.cylinder(2.35,0.14,"orangeLight",o,0,2.4,0);
}
,"flare-stack"(t,e,n){
  const o=oo(e,n,12.0);
  t.cylinder(0.35,10,"dark",o,0,5,0);
  for(let y of[2,4,6,8])t.box(1.2,0.15,1.2,"orange",o,0,y,0);
  t.cylinder(0.65,0.7,"orange",o,0,10.2,0);
  t.ball(0.7,1.2,0.7,"orangeLight",o,0,11.2,0);
}
,"cartello-salviamo-verde"(t,e,n){
  const o=oo(e,n,4.0);
  // The wooden signpost from the reference artwork
  t.box(2.6,0.4,1.4,"cream",o,0,0.2,0);
  t.ball(0.5,0.3,0.5,"foliage",o,-0.9,0.4,0.4);
  t.box(0.18,2.8,0.18,"dark",o,-0.85,1.4,0);
  t.box(0.18,2.8,0.18,"dark",o,0.85,1.4,0);
  t.box(2.8,1.4,0.16,"bark",o,0,2.3,0.08);
  t.box(2.7,0.06,0.18,"dark",o,0,2.75,0.09);
  t.box(2.7,0.06,0.18,"dark",o,0,2.3,0.09);
}
,"panchina-villa"(t,e,n){
  const o=oo(e,n,3.0);
  t.box(0.12,1.0,0.9,"foliage",o,-1.2,0.5,0);
  t.box(0.12,1.0,0.9,"foliage",o,1.2,0.5,0);
  t.cylinder(0.08,0.8,"dark",o,-1.2,0.85,0);
  t.cylinder(0.08,0.8,"dark",o,1.2,0.85,0);
  t.box(2.4,0.08,0.22,"bark",o,0,0.52,0.2);
  t.box(2.4,0.08,0.22,"bark",o,0,0.52,-0.05);
  t.box(2.4,0.18,0.08,"bark",o,0,0.82,-0.32);
  t.box(2.4,0.18,0.08,"bark",o,0,1.08,-0.36);
}
,"balustrata-xifonio"(t,e,n){
  const o=oo(e,n,4.0);
  t.box(3.8,0.35,0.6,"cream",o,0,0.18,0);
  for(let b=-2;b<=2;b++){
    t.cylinder(0.15,0.9,"cream",o,b*0.75,0.8,0);
    t.ball(0.22,0.22,0.22,"cream",o,b*0.75,0.7,0);
  }
  t.box(3.9,0.25,0.7,"cream",o,0,1.35,0);
}
,"vaso-terracotta-agave"(t,e,n){
  const o=oo(e,n,2.0);
  t.cylinder(0.5,0.8,"orange",o,0,0.4,0);
  t.cylinder(0.62,0.18,"orangeLight",o,0,0.85,0);
  t.ball(0.6,0.7,0.6,"foliage",o,0,1.2,0);
  t.ball(0.75,0.25,0.25,"leafLight",o,0.4,1.15,0);
  t.ball(0.75,0.25,0.25,"leafLight",o,-0.4,1.15,0);
}
,"gozzo-xifonio"(t,e,n){
  const o=oo(e,n,5.5);
  t.box(4.6,1.1,1.8,"blue",o,0,0.55,0,0.2);
  t.box(4.4,0.2,1.6,"cream",o,0,1.15,0);
  t.box(0.8,0.8,1.4,"orange",o,1.2,1.1,0);
  t.cylinder(0.08,2.4,"bark",o,-0.4,1.6,0);
}
,"cut-stump"(t,e,n){
  const o=oo(e,n,3.0);
  t.cylinder(1.4,1.1,"bark",o,0,0.55,0);
  t.cylinder(1.3,0.1,"orangeLight",o,0,1.12,0);
  t.ball(1.8,0.3,1.8,"bark",o,0,0.15,0);
}
,"chainsaw"(t,e,n){
  const o=oo(e,n,2.5);
  t.box(1.2,0.7,0.6,"orange",o,-0.2,0.6,0);
  t.cylinder(0.08,0.9,"dark",o,-0.9,0.9,0);
  t.box(1.6,0.3,0.06,"dark",o,1.0,0.5,0);
  t.cylinder(0.2,0.4,"dark",o,-0.5,0.4,0.35);
}
,"fountain-augusta"(t,e,n){
  const o=oo(e,n,4.0);
  t.cylinder(2.2,0.4,"cream",o,0,0.2,0);
  t.cylinder(1.9,0.2,"blueLight",o,0,0.35,0);
  t.cylinder(0.5,1.4,"cream",o,0,0.9,0);
  t.cylinder(1.2,0.3,"cream",o,0,1.7,0);
  t.ball(0.4,0.6,0.4,"blueLight",o,0,2.1,0);
}
,"heat-wave"(t,e,n){
  const o=oo(e,n,3.5);
  t.ball(1.8,1.2,0.4,"orangeLight",o,0,1.5,0);
  t.ball(1.2,0.8,0.3,"gold",o,-0.8,1.2,0);
  t.ball(1.2,0.8,0.3,"gold",o,0.8,1.8,0);
}
,"sewer-manhole"(t,e,n){
  const o=oo(e,n,1.8);
  t.cylinder(0.8,0.15,"dark",o,0,0.08,0);
  t.cylinder(0.65,0.08,"bark",o,0,0.18,0);
}
,"valvola-spurgo"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.42,1.2,"orange",o,0,0.6,0);
  t.cylinder(0.65,0.22,"dark",o,0,1.2,0);
  t.cylinder(0.12,0.8,"bark",o,0,1.6,0);
  t.cylinder(0.55,0.12,"gold",o,0,2.0,0);
}
,"chiatta-megara"(t,e,n){
  const o=oo(e,n,14.0);
  t.box(16,2.4,5.2,"bark",o,0,1.2,0,0.2);
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
  t.cylinder(0.10,7.5,"bark",o,10.0,8.0,0);
  t.box(2.2,2.0,2.2,"cream",o,10.0,4.0,0,0.1);
}
,"salvagente-rossini"(t,e,n){
  const o=oo(e,n,1.8);
  t.cylinder(0.08,2.2,"bark",o,0,1.1,0);
  t.ball(0.65,0.65,0.16,"cream",o,0,2.0,0.1);
  t.ball(0.32,0.32,0.22,"dark",o,0,2.0,0.1);
  t.ball(0.66,0.22,0.18,"orange",o,0,2.0,0.1);
}
,"pompa-idrovora"(t,e,n){
  const o=oo(e,n,2.5);
  t.box(2.4,1.6,1.8,"gold",o,0,0.8,0,0.15);
  t.cylinder(0.5,1.2,"dark",o,0.8,1.4,0);
  t.cylinder(0.22,2.8,"orange",o,-0.9,0.9,0.8);
  t.ball(0.35,0.35,0.35,"dark",o,-0.4,1.2,0);
}
,"cartello-divieto-balneazione"(t,e,n){
  const o=oo(e,n,2.8);
  t.cylinder(0.09,2.6,"dark",o,0,1.3,0);
  t.box(1.8,1.2,0.1,"cream",o,0,2.3,0.06);
  t.ball(0.45,0.45,0.12,"orange",o,0,2.3,0.07);
  t.box(0.6,0.14,0.14,"dark",o,0,2.3,0.08);
}
,"boa-filtrante"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.7,0.45,"orange",o,0,0.25,0);
  t.ball(0.7,0.5,0.7,"orangeLight",o,0,0.65,0);
  t.cylinder(0.08,1.2,"dark",o,0,1.2,0);
  t.ball(0.22,0.22,0.22,"gold",o,0,1.85,0);
}
,"tubo-scarico-mare"(t,e,n){
  const o=oo(e,n,4.2);
  t.cylinder(0.9,3.8,"dark",o,0,1.9,0);
  t.cylinder(1.05,0.25,"bark",o,0,0.6,0);
  t.cylinder(1.05,0.25,"bark",o,0,2.2,0);
  t.ball(0.75,0.75,0.75,"blue",o,0,0.1,0);
}
,"ombrellone-spiaggia"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(0.06,2.8,"cream",o,0,1.4,0);
  t.ball(1.6,0.35,1.6,"blue",o,0,2.7,0);
  t.ball(1.1,0.25,1.1,"cream",o,0,2.85,0);
}
,"sdraio-bagnante"(t,e,n){
  const o=oo(e,n,2.0);
  t.box(1.6,0.2,0.7,"bark",o,0,0.3,0);
  t.box(0.12,0.6,0.7,"blue",o,-0.7,0.5,0);
}
,"campanello-sos-costa"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.08,2.2,"orange",o,0,1.1,0);
  t.box(0.5,0.6,0.4,"orangeLight",o,0,1.8,0);
  t.ball(0.18,0.18,0.18,"gold",o,0,2.2,0);
}
,"traliccio-tubi"(t,e,n){
  const o=oo(e,n,8.0);
  t.box(0.3,8.0,0.3,"dark",o,-2.0,4.0,0);
  t.box(0.3,8.0,0.3,"dark",o,2.0,4.0,0);
  t.box(4.3,0.3,0.3,"dark",o,0,7.8,0);
  t.box(4.3,0.3,0.3,"dark",o,0,4.0,0);
  t.cylinder(0.4,7.8,"orange",o,-0.7,4.0,0);
  t.cylinder(0.32,7.8,"gold",o,0.7,4.0,0);
}
,"fusto-tossico"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.65,1.6,"dark",o,0,0.8,0);
  t.cylinder(0.68,0.12,"orange",o,0,0.3,0);
  t.cylinder(0.68,0.12,"orange",o,0,1.3,0);
  t.ball(0.22,0.22,0.22,"gold",o,0,1.65,0);
}
,"ciminiera-bicolore"(t,e,n){
  const o=oo(e,n,14.0);
  t.cylinder(1.4,12.0,"cream",o,0,6.0,0);
  for(let y=2;y<12;y+=4){
    t.cylinder(1.45,2.0,"orange",o,0,y,0);
  }
  t.ball(1.6,0.6,1.6,"dark",o,0,12.2,0);
}
,"manometro-pressione"(t,e,n){
  const o=oo(e,n,2.0);
  t.cylinder(0.15,1.6,"dark",o,0,0.8,0);
  t.cylinder(0.48,0.2,"cream",o,0,1.6,0);
  t.ball(0.12,0.12,0.12,"orange",o,0,1.6,0.12);
}
,"dirigibile-relique"(t,e,n){
  const o=oo(e,n,10.0);
  t.ball(4.8,1.6,1.6,"cream",o,0,2.2,0);
  t.box(1.4,0.6,0.7,"dark",o,0,0.9,0);
  t.box(0.1,1.2,1.2,"bark",o,-3.8,2.2,0);
}
,"cartello-bonifica"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(0.08,2.6,"dark",o,0,1.3,0);
  t.box(2.4,1.4,0.1,"orangeLight",o,0,2.4,0);
  t.box(2.2,1.2,0.12,"cream",o,0,2.4,0);
  t.ball(0.3,0.3,0.14,"orange",o,0,2.4,0);
}
,"pannello-amianto"(t,e,n){
  const o=oo(e,n,2.8);
  t.cylinder(0.08,2.2,"dark",o,0,1.1,0);
  t.box(1.6,1.1,0.08,"orange",o,0,2.0,0);
  t.box(1.4,0.9,0.10,"cream",o,0,2.0,0);
  t.box(0.7,0.18,0.12,"dark",o,0,2.0,0);
}
,"faro-cantiere"(t,e,n){
  const o=oo(e,n,4.2);
  t.cylinder(0.1,3.6,"dark",o,0,1.8,0);
  t.box(0.9,0.7,0.5,"orange",o,0,3.6,0);
  t.ball(0.35,0.35,0.1,"gold",o,0,3.6,0.28);
}
,"bidone-decontaminazione"(t,e,n){
  const o=oo(e,n,2.4);
  t.cylinder(0.7,1.8,"orange",o,0,0.9,0);
  t.cylinder(0.75,0.15,"cream",o,0,1.8,0);
  t.ball(0.25,0.25,0.25,"gold",o,0,1.9,0);
}
,"torre-sveva"(t,e,n){
  const o=oo(e,n,12.0);
  t.box(4.5,10.0,4.5,"cream",o,0,5.0,0,0.2);
  t.box(5.2,1.4,5.2,"cream",o,0,10.6,0);
  for(let i=-2;i<=2;i+=2){
    t.box(0.8,0.9,0.8,"cream",o,i,11.5,2.2);
    t.box(0.8,0.9,0.8,"cream",o,i,11.5,-2.2);
  }
}
,"stemma-federico"(t,e,n){
  const o=oo(e,n,2.8);
  t.box(1.8,2.2,0.2,"cream",o,0,1.4,0);
  t.ball(0.65,0.65,0.15,"gold",o,0,1.5,0.15);
  t.ball(0.4,0.4,0.18,"dark",o,0,1.5,0.18);
}
,"catapulta-antica"(t,e,n){
  const o=oo(e,n,3.8);
  t.box(3.2,0.4,1.8,"bark",o,0,0.2,0);
  t.cylinder(0.2,1.8,"dark",o,-1.2,0.2,0.9);
  t.cylinder(0.2,1.8,"dark",o,1.2,0.2,0.9);
  t.box(0.2,2.8,0.25,"bark",o,0,1.2,-0.2);
  t.ball(0.4,0.4,0.4,"cream",o,0,2.6,-0.4);
}
,"ponte-levatoio-svevo"(t,e,n){
  const o=oo(e,n,6.5);
  t.box(1.2,5.5,1.2,"cream",o,-2.4,2.75,0);
  t.box(1.2,5.5,1.2,"cream",o,2.4,2.75,0);
  t.box(4.6,0.3,3.4,"bark",o,0,0.2,1.4);
  t.cylinder(0.06,3.8,"dark",o,-2.2,3.2,1.2);
  t.cylinder(0.06,3.8,"dark",o,2.2,3.2,1.2);
}
,"lanterna-ferro-battuto"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(0.07,2.8,"dark",o,0,1.4,0);
  t.box(0.55,0.7,0.55,"dark",o,0,2.9,0);
  t.ball(0.28,0.38,0.28,"gold",o,0,2.9,0);
}
,"cannone-antico"(t,e,n){
  const o=oo(e,n,3.0);
  t.box(1.8,0.6,1.0,"bark",o,0,0.3,0);
  t.cylinder(0.35,0.14,"dark",o,-0.6,0.3,0.55);
  t.cylinder(0.35,0.14,"dark",o,0.6,0.3,0.55);
  t.cylinder(0.35,0.14,"dark",o,-0.6,0.3,-0.55);
  t.cylinder(0.35,0.14,"dark",o,0.6,0.3,-0.55);
  t.cylinder(0.26,2.2,"dark",o,0.2,0.7,0);
}
,"banco-posidonia"(t,e,n){
  const o=oo(e,n,3.0);
  t.ball(1.6,0.2,1.2,"dark",o,0,0.1,0);
  for(let p=-1;p<=1;p+=0.6){
    t.cylinder(0.06,1.4,"foliage",o,p,0.7,p*0.3);
    t.cylinder(0.06,1.2,"leafLight",o,p+0.2,0.6,-p*0.2);
  }
}
,"ancora-ammiragliato"(t,e,n){
  const o=oo(e,n,3.5);
  t.cylinder(0.14,3.2,"dark",o,0,1.6,0);
  t.cylinder(0.12,1.8,"bark",o,0,2.7,0);
  t.ball(0.7,0.4,0.4,"dark",o,0,0.4,0);
  t.ball(0.35,0.35,0.35,"gold",o,0,3.3,0);
}
,"falesia-calcarea"(t,e,n){
  const o=oo(e,n,8.0);
  t.box(7.0,5.0,3.5,"cream",o,0,2.5,0,0.3);
  t.box(5.5,3.0,2.8,"cream",o,0.8,4.5,0,0.25);
  t.ball(1.2,0.4,1.2,"foliage",o,-1.8,5.2,0.6);
}
,"campana-nebbia"(t,e,n){
  const o=oo(e,n,3.2);
  t.box(0.2,3.0,0.2,"bark",o,-0.8,1.5,0);
  t.box(0.2,3.0,0.2,"bark",o,0.8,1.5,0);
  t.box(1.8,0.2,0.2,"bark",o,0,2.9,0);
  t.cylinder(0.45,0.7,"gold",o,0,2.3,0);
}
,"gabbiano-scoglio"(t,e,n){
  const o=oo(e,n,2.0);
  t.box(1.4,0.8,1.2,"dark",o,0,0.4,0,0.2);
  t.ball(0.4,0.25,0.25,"cream",o,0,1.0,0);
  t.cylinder(0.04,0.25,"orange",o,0.35,1.0,0);
}
,"fenicottero-rosa"(t,e,n){
  const o=oo(e,n,3.5);
  t.cylinder(0.04,1.8,"orangeLight",o,-0.15,0.9,0);
  t.cylinder(0.04,1.8,"orangeLight",o,0.15,0.9,0);
  t.ball(0.55,0.35,0.35,"orangeLight",o,0,2.1,0);
  t.cylinder(0.06,1.2,"orangeLight",o,0.3,2.5,0);
  t.ball(0.18,0.14,0.14,"cream",o,0.4,3.1,0);
  t.cylinder(0.03,0.3,"dark",o,0.55,3.0,0);
}
,"paratoia-salina"(t,e,n){
  const o=oo(e,n,3.5);
  t.box(0.25,3.0,0.25,"bark",o,-1.2,1.5,0);
  t.box(0.25,3.0,0.25,"bark",o,1.2,1.5,0);
  t.box(2.2,1.8,0.15,"bark",o,0,1.2,0);
  t.cylinder(0.35,0.1,"dark",o,0,2.8,0);
}
,"badile-salinaio"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.05,2.0,"bark",o,0,1.0,0);
  t.box(0.5,0.6,0.06,"dark",o,0,0.3,0);
}
,"carrello-sale"(t,e,n){
  const o=oo(e,n,3.2);
  t.box(2.2,1.1,1.4,"dark",o,0,0.7,0,0.1);
  t.ball(0.9,0.6,0.6,"cream",o,0,1.2,0);
  t.cylinder(0.3,0.1,"bark",o,-0.7,0.3,0.75);
  t.cylinder(0.3,0.1,"bark",o,0.7,0.3,0.75);
  t.cylinder(0.3,0.1,"bark",o,-0.7,0.3,-0.75);
  t.cylinder(0.3,0.1,"bark",o,0.7,0.3,-0.75);
}
,"cannone-borbonico"(t,e,n){
  _D["cannone-antico"](t,e,n);
}
,"garitta-vedetta"(t,e,n){
  const o=oo(e,n,4.5);
  t.box(1.6,3.4,1.6,"cream",o,0,1.7,0,0.15);
  t.ball(1.1,0.9,1.1,"cream",o,0,3.6,0);
  t.box(0.6,1.4,0.1,"dark",o,0,2.0,0.8);
}
,"piramide-palle-cannone"(t,e,n){
  const o=oo(e,n,2.0);
  for(let x=-0.3;x<=0.3;x+=0.3){
    for(let z=-0.3;z<=0.3;z+=0.3){
      t.ball(0.18,0.18,0.18,"dark",o,x,0.18,z);
    }
  }
  t.ball(0.18,0.18,0.18,"dark",o,0,0.48,0);
}
,"argano-catena-porto"(t,e,n){
  const o=oo(e,n,3.0);
  t.box(0.2,2.2,0.8,"dark",o,-0.9,1.1,0);
  t.box(0.2,2.2,0.8,"dark",o,0.9,1.1,0);
  t.cylinder(0.5,1.6,"bark",o,0,1.4,0);
  t.cylinder(0.65,0.1,"gold",o,1.0,1.4,0);
}
,"bandiera-sicilia"(t,e,n){
  const o=oo(e,n,4.8);
  t.cylinder(0.06,4.5,"dark",o,0,2.25,0);
  t.box(1.6,0.6,0.04,"orange",o,0.8,3.9,0);
  t.box(1.6,0.6,0.04,"gold",o,0.8,3.3,0);
  t.ball(0.25,0.25,0.06,"cream",o,0.8,3.6,0.02);
}
,"vaso-caltagirone"(t,e,n){
  const o=oo(e,n,2.2);
  t.cylinder(0.45,0.9,"cream",o,0,0.45,0);
  t.cylinder(0.6,0.2,"blue",o,0,0.9,0);
  t.ball(0.65,0.7,0.65,"foliage",o,0,1.3,0);
  t.ball(0.22,0.22,0.22,"gold",o,0.3,1.3,0.4);
  t.ball(0.22,0.22,0.22,"orange",o,-0.3,1.4,-0.3);
}
,"palina-raccolta-differenziata"(t,e,n){
  const o=oo(e,n,2.4);
  t.cylinder(0.06,2.0,"dark",o,0,1.0,0);
  t.box(0.4,0.6,0.3,"blue",o,-0.45,1.3,0);
  t.box(0.4,0.6,0.3,"gold",o,0,1.3,0);
  t.box(0.4,0.6,0.3,"foliage",o,0.45,1.3,0);
}
,"arco-trionfale-verde"(t,e,n){
  const o=oo(e,n,8.0);
  t.cylinder(0.5,6.0,"foliage",o,-3.0,3.0,0);
  t.cylinder(0.5,6.0,"foliage",o,3.0,3.0,0);
  t.ball(2.0,1.2,1.2,"leafLight",o,-2.6,6.0,0);
  t.ball(2.0,1.2,1.2,"leafLight",o,2.6,6.0,0);
  t.ball(3.2,1.2,1.4,"foliage",o,0,6.6,0);
  t.ball(0.4,0.4,0.4,"gold",o,0,6.8,0.6);
  t.ball(0.3,0.3,0.3,"orange",o,-1.4,6.4,0.6);
  t.ball(0.3,0.3,0.3,"orange",o,1.4,6.4,0.6);
}
,"scarico-fogna-liquami"(t,e,n){
  const o=oo(e,n,3.2);
  t.cylinder(0.8,0.8,"dark",o,0,0.8,0);
  t.cylinder(0.65,0.7,"dark",o,0,0.8,0.1);
  t.cylinder(0.5,1.8,"orange",o,0,0.3,0.4);
  t.ball(1.2,0.25,1.0,"dark",o,0,0.1,0.9);
}
,"ciminiera-fumo-animata"(t,e,n){
  const o=oo(e,n,14.0);
  t.cylinder(1.2,10.0,"cream",o,0,5.0,0);
  t.cylinder(1.25,2.0,"orange",o,0,2.5,0);
  t.cylinder(1.25,2.0,"orange",o,0,7.5,0);
  t.ball(1.8,1.2,1.8,"dark",o,0,10.8,0);
  t.ball(2.6,1.6,2.4,"dark",o,0.8,12.2,0.3);
  t.ball(3.4,2.0,3.0,"dark",o,-1.0,14.0,-0.4);
}
,"discarica-abusiva"(t,e,n){
  const o=oo(e,n,4.0);
  t.box(2.2,0.6,1.8,"dark",o,0,0.3,0,0.2);
  t.cylinder(0.45,0.9,"orange",o,-0.8,0.5,0.4);
  t.box(0.9,0.8,0.6,"cream",o,0.7,0.5,-0.3);
  t.ball(0.5,0.5,0.5,"bark",o,0.1,0.8,0.2);
  t.box(1.2,0.2,0.8,"dark",o,-0.2,0.9,-0.2);
}
,"liquame-tossico-pozza"(t,e,n){
  const o=oo(e,n,3.0);
  t.ball(1.8,0.12,1.4,"orangeLight",o,0,0.06,0);
  t.ball(1.2,0.10,0.9,"gold",o,0.2,0.08,0.1);
}
,"fusto-tossico-sversato"(t,e,n){
  const o=oo(e,n,2.5);
  t.cylinder(0.55,1.4,"dark",o,0,0.55,0);
  t.cylinder(0.58,0.1,"orange",o,0,0.55,0.4);
  t.ball(1.2,0.08,0.9,"orangeLight",o,0.8,0.04,0);
}
,"fumo-petrolchimico-nube"(t,e,n){
  const o=oo(e,n,8.0);
  t.ball(3.6,1.8,2.4,"dark",o,0,3.0,0);
  t.ball(2.8,1.5,2.0,"dark",o,-2.0,3.5,0.5);
  t.ball(2.5,1.4,1.8,"dark",o,1.8,3.2,-0.5);
  t.ball(2.0,1.2,1.6,"orange",o,0.5,4.0,0.2);
}
,"torcia-petrolchimico-fiamma"(t,e,n){
  const o=oo(e,n,9.0);
  t.cylinder(0.25,7.0,"dark",o,0,3.5,0);
  t.cylinder(0.5,0.6,"orange",o,0,7.0,0);
  t.ball(0.8,1.4,0.8,"orangeLight",o,0,8.0,0);
  t.ball(0.5,0.9,0.5,"gold",o,0,8.2,0);
}
,"rifiuti-plastica-costa"(t,e,n){
  const o=oo(e,n,2.2);
  t.ball(0.4,0.15,0.3,"blueLight",o,-0.5,0.1,0.2);
  t.cylinder(0.12,0.5,"cream",o,0.3,0.1,-0.2);
  t.box(0.4,0.3,0.3,"orange",o,0,0.15,0.4);
}
,"fiume-petrolio-greggio"(t,e,n){
  const o=oo(e,n,8.0);
  t.box(8.0,0.35,3.6,"dark",o,0,0.18,0,0.1);
  t.box(7.2,0.20,3.0,"dark",o,0,0.32,0);
  t.ball(1.8,0.12,1.2,"orange",o,-2.0,0.38,0.4);
  t.ball(1.5,0.10,1.0,"gold",o,1.8,0.38,-0.5);
  t.ball(1.2,0.08,0.8,"blue",o,0,0.38,0.3);
  t.ball(0.4,0.3,0.4,"dark",o,-1.2,0.45,-0.3);
  t.ball(0.5,0.35,0.5,"dark",o,0.8,0.48,0.5);
  t.ball(0.3,0.2,0.3,"dark",o,2.5,0.42,0.2);
}
,"colata-cemento-fresco"(t,e,n){
  const o=oo(e,n,7.0);
  t.box(7.0,0.45,3.4,"cream",o,0,0.22,0,0.15);
  t.box(5.8,0.30,2.6,"cream",o,0.4,0.42,0);
  t.box(7.2,0.6,0.15,"bark",o,0,0.3,1.7);
  t.box(7.2,0.6,0.15,"bark",o,0,0.3,-1.7);
  t.cylinder(0.12,1.2,"bark",o,-3.2,0.6,1.8);
  t.cylinder(0.12,1.2,"bark",o,0,0.6,1.8);
  t.cylinder(0.12,1.2,"bark",o,3.2,0.6,1.8);
  t.ball(1.4,0.15,1.2,"dark",o,-1.5,0.48,0.2);
  t.ball(1.6,0.15,1.3,"dark",o,1.6,0.48,-0.3);
}
,"rogo-tossico-pneumatici"(t,e,n){
  const o=oo(e,n,6.0);
  t.cylinder(1.2,0.5,"dark",o,-0.6,0.25,0);
  t.cylinder(1.1,0.5,"dark",o,0.7,0.25,-0.4);
  t.cylinder(1.0,0.45,"dark",o,0.2,0.6,0.2);
  t.cylinder(0.9,0.45,"dark",o,-0.4,0.85,-0.2);
  t.ball(1.6,1.8,1.4,"orange",o,0,1.5,0);
  t.ball(1.2,1.5,1.0,"orangeLight",o,0.3,2.2,0.1);
  t.ball(0.8,1.2,0.7,"gold",o,-0.2,2.6,-0.1);
  t.ball(1.8,1.4,1.8,"dark",o,0.5,3.6,0.2);
  t.ball(2.4,1.8,2.2,"dark",o,-0.4,4.8,-0.3);
  t.ball(3.0,2.2,2.8,"dark",o,0.8,6.2,0.4);
}
,"barriera-panne-anti-petrolio"(t,e,n){
  const o=oo(e,n,6.0);
  for(let i=-2.4;i<=2.4;i+=1.2){
    t.cylinder(0.35,1.1,"gold",o,i,0.35,0,0,0,Math.PI/2);
    t.cylinder(0.08,0.2,"dark",o,i+0.6,0.35,0,0,0,Math.PI/2);
  }
  t.box(5.8,0.6,0.08,"dark",o,0,-0.1,0);
}
,"idrante-civico-acqua"(t,e,n){
  const o=oo(e,n,3.0);
  t.cylinder(0.45,0.2,"dark",o,0,0.1,0);
  t.cylinder(0.32,1.6,"orange",o,0,0.9,0);
  t.ball(0.38,0.32,0.38,"orange",o,0,1.75,0);
  t.cylinder(0.12,0.25,"gold",o,0,1.95,0);
  t.cylinder(0.18,0.35,"gold",o,0.35,1.1,0,0,0,Math.PI/2);
  t.cylinder(0.18,0.35,"gold",o,-0.35,1.1,0,0,0,Math.PI/2);
  t.cylinder(0.22,0.3,"gold",o,0,1.2,0.35,Math.PI/2,0,0);
}
,"fiume-fognatura-reflui"(t,e,n){
  const o=oo(e,n,7.5);
  t.box(7.5,0.4,3.2,"dark",o,0,0.2,0,0.1);
  t.ball(1.6,0.12,1.2,"orangeLight",o,-1.8,0.36,0.3);
  t.ball(2.0,0.14,1.4,"cream",o,1.2,0.38,-0.2);
  t.ball(1.2,0.12,1.0,"cream",o,-0.2,0.40,0.5);
}
,"paratoia-idraulica-metallo"(t,e,n){
  const o=oo(e,n,4.5);
  t.box(0.3,4.2,0.4,"dark",o,-1.4,2.1,0);
  t.box(0.3,4.2,0.4,"dark",o,1.4,2.1,0);
  t.box(3.2,0.4,0.5,"dark",o,0,4.2,0);
  t.box(2.6,2.2,0.18,"dark",o,0,1.3,0);
  t.cylinder(0.12,3.4,"gold",o,0,2.6,0);
  t.cylinder(0.55,0.14,"orange",o,0,4.4,0);
}
'''
