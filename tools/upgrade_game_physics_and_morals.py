# tools/upgrade_game_physics_and_morals.py
import os
import re

print("=== UPGRADING AUGUSTA GAME: SOLID PHYSICS & CIVIC MORALS ===")

# --- 1. UPDATE tools/generate_all_10_levels.py ---
with open("tools/generate_all_10_levels.py", "r", encoding="utf-8") as f:
    gen_content = f.read()

# Define the 10 civic morals
morals = {
    1: {
        "title": "I Polmoni Verdi di Augusta: Il Valore Inestimabile dei Ficus Secolari",
        "story": "I grandi Ficus della Villa Comunale furono piantati nel 1850. Non sono semplici alberi: sono giganti gentili che da oltre 170 anni ci donano ombra fresca, abbassano la temperatura estiva fino a 5 gradi e ripuliscono l'aria dallo smog. Tagliare un albero antico significa cancellare un pezzo della nostra salute e della memoria di Augusta. Ricordate, piccoli e grandi: piantare e curare un albero è il più bell'atto d'amore che possiamo fare per la nostra città!"
    },
    2: {
        "title": "Il Mare è la Nostra Vita: Stop agli Scarichi e Fognature nel Golfo",
        "story": "Augusta è un'isola circondata dal mare ionico, ma per decenni scarichi fognari non depurati e allagamenti hanno ferito le nostre coste. Quando il mare si inquina, i pesci muoiono e i bambini perdono il diritto di fare il bagno sotto casa. Non gettare rifiuti nei tombini e pretendere depuratori moderni ed efficienti è un dovere civico. Il mare pulito è un tesoro di tutti!"
    },
    3: {
        "title": "Il Respiro di Augusta: Diritto alla Salute e Transizione Ecologica",
        "story": "Dagli anni '50, le imponenti ciminiere delle raffinerie hanno segnato l'orizzonte di Augusta. Hanno portato lavoro nel dopoguerra, ma anche veleni, fumi acri e sofferenza. Nessuna famiglia dovrebbe mai dover scegliere tra salute e stipendio. La vera sfida del domani è la transizione ecologica: bonificare i terreni, bloccare le emissioni nocive e investire sulle energie rinnovabili!"
    },
    4: {
        "title": "L'Hangar dei Dirigibili: Proteggere la Storia dalla Speculazione e dal Degrado",
        "story": "Costruito nel 1920 con un'audace volta parabolica in cemento armato, l'Hangar di Augusta è un monumento di ingegneria aeronautica unico al mondo. Per troppo tempo è rimasto abbandonato tra discariche e cemento selvaggio. I monumenti storici sono la nostra identità: restaurarli e trasformarli in parchi culturali significa dare futuro e orgoglio alle nuove generazioni!"
    },
    5: {
        "title": "Il Castello Svevo (1232): La Nostra Fortezza non Deve Crollare",
        "story": "Voluto da Federico II di Svevia oltre 800 anni fa, il Castello Svevo ha resistito a guerre e terremoti, ma rischia di sgretolarsi per la salsedine, il moto ondoso e l'abbandono. Il nostro patrimonio antico non è eterno: va tutelato ogni giorno con restauri costanti e rispetto. Custodire le fortezze di ieri ci insegna a essere cittadini forti e consapevoli domani!"
    },
    6: {
        "title": "Faro di Capo Santa Croce: La Bellezza Costiera contro i Roghi Tossici",
        "story": "Sulle maestose falesie bianche di Capo Santa Croce, dove il faro guida i naviganti, mani criminali hanno spesso bruciato copertoni e rifiuti. I roghi tossici sprigionano diossine che avvelenano l'aria che respiriamo. Rispettare i sentieri, non abbandonare immondizia e denunciare gli incivili è l'unico modo per tenere accesa la luce della legalità e della civiltà!"
    },
    7: {
        "title": "Le Saline Regie: Oasi Fragile di Fenicotteri e Biodiversità",
        "story": "Sfruttate fin dall'antichità per estrarre l'oro bianco del sale, le Saline di Augusta sono un paradiso umido dove nidificano aironi e fenicotteri rosa. Gli sversamenti abusivi rischiano di distruggere questo delicato ecosistema. Imparare ad amare la natura nei suoi piccoli dettagli è il primo passo per proteggerla: gli animali non hanno voce, siamo noi la loro voce!"
    },
    8: {
        "title": "Forte Vittoria (1567): Il Riscatto e la Bonifica della Rada Portuale",
        "story": "Forte Vittoria sorge fiero in mezzo al mare della rada megarese fin dal Rinascimento. Il porto è il cuore operoso della città, ma sui fondali riposano ancora fanghi industriali da bonificare. Usare panne galleggianti e ripulire il bacino navale è un impegno verso il futuro: il mare di Augusta deve tornare ad essere limpido e sicuro per pescatori e naviganti!"
    },
    9: {
        "title": "Le Terrazze del Tauro: Prevenzione Incendi e Difesa del Suolo",
        "story": "Dalle colline del Tauro si scorge l'azzurro del golfo tra ulivi e mandorli secolari. Purtroppo, ogni estate i piromani bruciano ettari di macchia mediterranea, causando frane ed erosione. Curare i boschi, avvisare tempestivamente i soccorsi se si avvista fumo e piantare nuovi arbusti autoctoni è la nostra barriera più sicura contro frane e desertificazione!"
    },
    10: {
        "title": "Porta Spagnola (1692): Il Trionfo dell'Utopia Verde di Augusta",
        "story": "Varcare la solenne Porta Spagnola, edificata nel 1692, segna il trionfo dell'avventura ecologica: la dimostrazione vivente che Augusta può rinascere dalle sue ferite industriali, con alberi centenari rispettati, acque balneabili, aria pulita e monumenti vivi. Ricorda: il futuro verde di Augusta non è una favola, ma una realtà che vive nelle mani e nel cuore di chi ama questa terra!"
    }
}

for i in range(1, 11):
    m_info = morals[i]
    # Inject moralTitle and moralStory right after intro: "..."
    # Pattern: const augustaL{i} = yr({ ... intro: "..."
    intro_pattern = rf'(const augustaL{i}\s*=\s*yr\(\{{[\s\S]*?intro:\s*"[^"]*",)'
    replacement = rf'\1\n  moralTitle: "{m_info["title"]}",\n  moralStory: "{m_info["story"]}",'
    gen_content = re.sub(intro_pattern, replacement, gen_content, count=1)

# Platform gap fixes in Level 1
gen_content = gen_content.replace(
    'S("lift-canopy", 28, 3.6, 14.8, "lift", {moveX: 2.5, period: 4.2}),\n    S("plat-avenue", 35, 8.0, 15.2, "stone"),\n    S("spring-branch1", 42, 2.0, 15.2, "spring"),',
    'S("lift-canopy", 28, 4.2, 14.8, "lift", {moveX: 2.5, period: 4.2}),\n    S("plat-avenue", 34.0, 8.5, 15.2, "stone"),\n    S("spring-branch1", 42.5, 2.0, 15.2, "spring"),\n    S("step-crossing-roots", 44.5, 3.5, 15.2, "stone"),'
)
gen_content = gen_content.replace(
    'S("pulse-stump2", 180, 3.8, 15.6, "pulse", {period: 4.2, phase: 0.5}),\n    S("plat-fountain", 187, 7.0, 15.0, "stone"),',
    'S("pulse-stump2", 180, 4.8, 15.6, "pulse", {period: 4.2, phase: 0.5}),\n    S("plat-fountain", 186.0, 8.0, 15.0, "stone"),'
)
gen_content = gen_content.replace(
    'S("spring-piazza", 200, 2.0, 15.8, "spring"),\n    S("plat-terrace-piazza", 204, 8.0, 16.0, "stone", {landmark: "sandwheel"}),',
    'S("spring-piazza", 199.5, 2.0, 15.8, "spring"),\n    S("step-crossing-piazza", 201.2, 3.2, 15.9, "stone"),\n    S("plat-terrace-piazza", 204, 9.0, 16.0, "stone", {landmark: "sandwheel"}),'
)

# Platform gap fixes in Level 2
gen_content = gen_content.replace(
    'S("lift-crane-seawall", 20, 3.5, 10.8, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-quay-promenade", 27, 8.0, 11.5, "stone"),\n    S("spring-seawall", 34, 2.0, 11.5, "spring"),',
    'S("lift-crane-seawall", 20, 4.0, 10.8, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-quay-promenade", 25.5, 9.0, 11.5, "stone"),\n    S("spring-seawall", 34.5, 2.0, 11.5, "spring"),\n    S("step-crossing-sewer", 36.5, 3.5, 11.6, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-outer-link", 197, 3.5, 13.5, "ledge"),\n    S("pit-sewage-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-molo-nord", 204, 8.0, 13.5, "stone"',
    'S("step-outer-link", 197, 4.5, 13.5, "ledge"),\n    S("pit-sewage-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-molo-nord", 203, 8.5, 13.5, "stone"'
)

# Platform gap fixes in Level 3
gen_content = gen_content.replace(
    'S("lift-cracker-climb", 22, 3.5, 12.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-distillation-deck", 29, 8.0, 12.8, "stone"),\n    S("spring-petrol", 36, 2.0, 12.8, "spring"),',
    'S("lift-cracker-climb", 22, 4.0, 12.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-distillation-deck", 27.5, 8.5, 12.8, "stone"),\n    S("spring-petrol", 36, 2.0, 12.8, "spring"),\n    S("step-crossing-petrol", 38.0, 3.5, 12.8, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-ref-link", 197, 3.5, 14.5, "ledge"),\n    S("pit-oil-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-ref-exit", 204, 8.0, 14.5, "stone"',
    'S("step-ref-link", 197, 4.5, 14.5, "ledge"),\n    S("pit-oil-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-ref-exit", 203, 8.5, 14.5, "stone"'
)

# Platform gap fixes in Level 4
gen_content = gen_content.replace(
    'S("lift-silo-crane", 22, 3.5, 13.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-mixer-hopper", 29, 8.0, 13.8, "stone"),\n    S("spring-cement", 36, 2.0, 13.8, "spring"),',
    'S("lift-silo-crane", 22, 4.0, 13.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-mixer-hopper", 27.5, 8.5, 13.8, "stone"),\n    S("spring-cement", 36, 2.0, 13.8, "spring"),\n    S("step-crossing-cement", 38.0, 3.5, 13.8, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-hang-link", 197, 3.5, 15.5, "ledge"),\n    S("pit-cement-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-hang-exit", 204, 8.0, 15.5, "stone"',
    'S("step-hang-link", 197, 4.5, 15.5, "ledge"),\n    S("pit-cement-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-hang-exit", 203, 8.5, 15.5, "stone"'
)

# Platform gap fixes in Level 5
gen_content = gen_content.replace(
    'S("lift-moat-crane", 22, 3.5, 14.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-moat-edge", 29, 8.0, 14.8, "stone"),\n    S("spring-castle", 36, 2.0, 14.8, "spring"),',
    'S("lift-moat-crane", 22, 4.0, 14.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-moat-edge", 27.5, 8.5, 14.8, "stone"),\n    S("spring-castle", 36, 2.0, 14.8, "spring"),\n    S("step-crossing-castle", 38.0, 3.5, 14.8, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-keep-link", 197, 3.5, 16.5, "ledge"),\n    S("pit-castle-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-keep-entrance", 204, 8.0, 16.5, "stone"',
    'S("step-keep-link", 197, 4.5, 16.5, "ledge"),\n    S("pit-castle-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-keep-entrance", 203, 8.5, 16.5, "stone"'
)

# Platform gap fixes in Level 6
gen_content = gen_content.replace(
    'S("lift-reef-funicular", 22, 3.5, 15.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-headland-ledge", 29, 8.0, 15.8, "stone"),\n    S("spring-cliff", 36, 2.0, 15.8, "spring"),',
    'S("lift-reef-funicular", 22, 4.0, 15.0, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-headland-ledge", 27.5, 8.5, 15.8, "stone"),\n    S("spring-cliff", 36, 2.0, 15.8, "spring"),\n    S("step-crossing-cliff", 38.0, 3.5, 15.8, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-lantern-link", 197, 3.5, 17.5, "ledge"),\n    S("pit-cliff-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-clf-exit", 204, 8.0, 17.5, "stone"',
    'S("step-lantern-link", 197, 4.5, 17.5, "ledge"),\n    S("pit-cliff-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-clf-exit", 203, 8.5, 17.5, "stone"'
)

# Platform gap fixes in Level 7
gen_content = gen_content.replace(
    'S("lift-windmill-paddle", 22, 3.5, 13.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-crystallizer", 29, 8.0, 14.2, "stone"),\n    S("spring-salt", 36, 2.0, 14.2, "spring"),',
    'S("lift-windmill-paddle", 22, 4.0, 13.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-crystallizer", 27.5, 8.5, 14.2, "stone"),\n    S("spring-salt", 36, 2.0, 14.2, "spring"),\n    S("step-crossing-salt", 38.0, 3.5, 14.2, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-mill-link", 197, 3.5, 16.0, "ledge"),\n    S("pit-salt-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-slt-exit", 204, 8.0, 16.0, "stone"',
    'S("step-mill-link", 197, 4.5, 16.0, "ledge"),\n    S("pit-salt-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-slt-exit", 203, 8.5, 16.0, "stone"'
)

# Platform gap fixes in Level 8
gen_content = gen_content.replace(
    'S("lift-launch-deck", 22, 3.5, 15.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-chain-capstan", 29, 8.0, 16.2, "stone"),\n    S("spring-fort", 36, 2.0, 16.2, "spring"),',
    'S("lift-launch-deck", 22, 4.0, 15.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-chain-capstan", 27.5, 8.5, 16.2, "stone"),\n    S("spring-fort", 36, 2.0, 16.2, "spring"),\n    S("step-crossing-fort", 38.0, 3.5, 16.2, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-keep-link2", 197, 3.5, 18.0, "ledge"),\n    S("pit-fort-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-frt-exit", 204, 8.0, 18.0, "stone"',
    'S("step-keep-link2", 197, 4.5, 18.0, "ledge"),\n    S("pit-fort-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-frt-exit", 203, 8.5, 18.0, "stone"'
)

# Platform gap fixes in Level 9
gen_content = gen_content.replace(
    'S("lift-terrace-funicular", 22, 3.5, 16.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-drystone-wall", 29, 8.0, 17.2, "stone"),\n    S("spring-scrub", 36, 2.0, 17.2, "spring"),',
    'S("lift-terrace-funicular", 22, 4.0, 16.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-drystone-wall", 27.5, 8.5, 17.2, "stone"),\n    S("spring-scrub", 36, 2.0, 17.2, "spring"),\n    S("step-crossing-scrub", 38.0, 3.5, 17.2, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-belvedere-link", 197, 3.5, 19.0, "ledge"),\n    S("pit-scrub-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-tauro-exit", 204, 8.0, 19.0, "stone"',
    'S("step-belvedere-link", 197, 4.5, 19.0, "ledge"),\n    S("pit-scrub-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-tauro-exit", 203, 8.5, 19.0, "stone"'
)

# Platform gap fixes in Level 10
gen_content = gen_content.replace(
    'S("lift-isthmus-gantry", 22, 3.5, 17.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-bastion-san-giacomo", 29, 8.0, 18.2, "stone"),\n    S("spring-porta", 36, 2.0, 18.2, "spring"),',
    'S("lift-isthmus-gantry", 22, 4.0, 17.5, "lift", {moveY: 2.0, period: 4.0}),\n    S("plat-bastion-san-giacomo", 27.5, 8.5, 18.2, "stone"),\n    S("spring-porta", 36, 2.0, 18.2, "spring"),\n    S("step-crossing-porta", 38.0, 3.5, 18.2, "stone"),'
)
gen_content = gen_content.replace(
    'S("step-parvis-link", 197, 3.5, 20.0, "ledge"),\n    S("pit-porta-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-prt-exit", 204, 8.0, 20.0, "stone"',
    'S("step-parvis-link", 197, 4.5, 20.0, "ledge"),\n    S("pit-porta-3", 152, 48, 2.0, "stone", {spiked: !0}),\n\n    S("dock-prt-exit", 203, 8.5, 20.0, "stone"'
)

with open("tools/generate_all_10_levels.py", "w", encoding="utf-8") as f:
    f.write(gen_content)
print("[✓] Updated tools/generate_all_10_levels.py with civic morals and gap bridges!")

# Execute generation
import subprocess
res = subprocess.run(["python3", "tools/generate_all_10_levels.py"], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Error:", res.stderr)
