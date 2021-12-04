import random
text1 = ["Che facciamo stasera, Marco, usciamo?","Volentieri! Che ne dici di andare al cinema?","È una buona idea! Sai che film danno al ”Lux”?"," Un giallo di Dario Argento; all Imperiale, invece, c’è una commedia allitaliana con Alberto Sordi. Quale scegliamo?", "Mah! Forse è meglio il secondo. Qual è il titolo? ","In viaggio con papà.","Ah, sì! So che è molto divertente.", "Chiediamo a Giorgio e Paola se vogliono venire con noi?" ,"D’accordo, adesso telefono!" ,"Sì, così facciamo in tempo per lo spettacolo delle dieci e mezzo."]
trans1 = ["-ЧТО ДЕЛАЕМ СЕГОДНЯ ВЕЧЕРОМ, СХОДИМ КУДА НИБУДЬ?","-С УДОВОЛЬСТВИЕМ! ЧТО СКАЖЕШЬ НА СЧЁТ ТОГО ЧТОБЫ СХОДИШЬ В КИНО?","-ЧУДЕСНАЯ ИДЕЯ! ЗНАЕШЬ КАКОЙ ФИЛЬМ ПОКАЗЫВАЮТ В ЛЮКС?","-ДЕТЕКТИВ ДАРИО ОРДЖЕНТИ, В ИМПЕРИАЛЕ, НАОБОРОТ, КОМЕДИЯ В ИТАЛЬЯНСОКМ СТИЛЕ С АЛЬБЕРТО СОРДИ. КАКОЙ ВЫБЕРЕМ?","-НЕ ЗНАЮ. МОЖЕТ ЛУЧШЕ ВТОРОЙ, КАКОЕ НАЗВАНИЕ?","-В ПУТЕШЕСТВИЕ С ПАПОЙ","-АХ ДА, ЗНАЮ ЧТО ОН ОЧЕНЬ ЗАБАВНЫЙ!"," ПОЗОВЁМ ЖИОРЖИО И ПАУЛО ОНИ ХОТЯТ ПОЙТИ С НАМИ?","-КОНЕЧНО, СЕЙЧАС ПОЗВОНЮ.","-ДА, ТАК УСПЕЕМ ВОВРЕМЯ НА СПЕКТАКЛЬ В 10 30"]

text2 =["Dal lunedì al venerdì io e i miei genitori ci alziamo presto."," Mamma e papà si svegliano alle sei e mezza, fanno colazione, si lavano e poi vanno al lavoro verso le sette e mezza."," Io sento come si muovono e chiudono la porta, poi mi alzo anch’io, mi metto le ciabatte e la vestaglia, mi lavo il viso, faccio colazione, poi torno in bagno, mi lavo i denti e mi vesto."," Prendo il mio zaino e scendo, saluto i nonni ed esco. ","I nonni, che sono pensionati, si svegliano presto, alle sei, ma rimangono a letto fino alle nove. ","Poi si alzano, la nonna fa i lavori di casa e comincia a preparare il pranzo. ","Il nonno va a comprare il pane ed il latte e spesso va al mercato. ","Il mercato non c’è tutti i giorni nello stesso posto, si sposta di paese in paese, ed il nonno si ricorda perfettamente dove si trova il mercato il lunedì, il martedì, il mercoledì… ","Siccome si muove in bicicletta, si stanca molto, e quando torna va subito a riposarsi.","La mamma lavora dalle otto alle due, poi torna a casa e pranza assieme alla nonna. ","Due volte la settimana, il lunedì ed il mercoledì, lavora anche al pomeriggio, dalle due alle cinque. ","Visto che non le piace mangiare un panino in ufficio, lei torna a casa, pranza e chiacchiera un po’ con i nonni. ","Papà invece non torna a casa a mangiare, perché va in mensa. ","Dice che il cibo della mensa non è molto buono, ma almeno può distrarsi un po’ con i suoi colleghi e non pensare al lavoro per qualche tempo."," Di solito finisce di lavorare alle cinque, anche se qualche volta fa gli straordinari e rimane al lavoro di più.","Io vado all’università tutti i giorni."," Se ho una lezione alla mattina e una al pomeriggio, cosa che succede molto spesso, rimango all’università: studio, navigo su Internet, passo un po’ di tempo con i miei amici. ","Ogni tanto mi capita di non andare ad una lezione a causa del lavoro: mi dispiace sempre molto perdere le lezioni, ma mi dispiace ancora di più non vedere i bambini!","Torno a casa verso le sette o le otto, e a quell’ora ci riuniamo tutti per cena. ","Mangiamo in cucina quello che la mamma prepara il pomeriggio e ci raccontiamo ciò che ci è successo durante il giorno. ","Poi ci sediamo in salotto e guardiamo la televisione…Ovviamente prima io o la mamma sparecchiamo la tavola e laviamo i piatti." ]
trans2 = ["С понедельника по пятницу мы с родителями рано вставаем. ","Мама и папа просыпаются в 6: 30, завтракают, моются, а затем идут на работу к 7: 30. ","Я слышу, как они двигаются и закрывают дверь, а потом я встаю, надеваю тапочки и халат, моюсь, завтракаю, потом возвращаюсь в ванную, чищу зубы и одеваюсь.","Я беру свой рюкзак и спускаюсь, прощаюсь с бабушкой и дедушкой и выхожу. ","Бабушка и дедушка, которые являются пенсионерами, просыпаются рано, в шесть, но остаются в постели до девяти. ","Затем они встают, бабушка делает домашнюю работу и начинает готовить обед. ","Дедушка ходит покупать хлеб и молоко и часто ходит на рынок. ","Рынок не находится каждый день на одном месте, он перемещается из города в город, и дедушка прекрасно помнит, где рынок находится в понедельник, вторник, среда... ","так как он перемещается на велосипеде, он очень устает, и когда он возвращается сразу же отдохнуть.","Мама работает с восьми до двух, а затем возвращается домой и обедает вместе с бабушкой. ","Два раза в неделю, по понедельникам и средам, также работает во второй половине дня, от двух до пяти. ","Поскольку она не любит есть бутерброд в офисе, она возвращается домой, обедает и немного болтает с бабушкой и дедушкой. ","Папа не приходит домой, чтобы поесть, потому что он ходит в столовую."," Он говорит, что еда в столовой не очень хороша, но, по крайней мере, она может немного отвлечься со своими коллегами и не думать о работе в течение некоторого времени."," Обычно он заканчивает работу в пять, хотя иногда он делает сверхурочные и остается на работе больше. ","Я хожу в университет каждый день. ","Если у меня занятия утром и днем, что бывает очень часто, я остаюсь в университете: учусь, сижу в Интернете, провожу время с моими друзьями. ","Время от времени я не собираюсь идти на урок из-за работы: я всегда очень сожалею о том, чтобы пропустить уроки,но я сожалею еще больше не вижу детей!","Я прихожу домой около семи или восьми, и в тот час мы все собираемся вместе на ужин. ","Мы едим на кухне то, что мама готовит днем, и мы рассказываем, что произошло в течение дня."," Затем мы сидим в гостиной и смотрим телевизор, конечно, сначала мы или мама убираем стол и моем посуду."]

text3 =["Buongiorno! Due sì! Sì, è a nome… Il tavolo è quello lì?"," Beh, carino, no? Sì, sì. Ci vieni spesso?"," Beh, fin da bambino con i miei genitori e ora con gli amici."," Mi è sempre piaciuta l’atmosfera.","Sì e poi... c’è un buon odorino!","Già.... Beh, non so tu, ma io ho una favme!","Uh, quante cose buone! Dunque, vediamo... Cosa mi consigli?","Ah, qui fanno degli antipasti buonissimi. Leggi qui: “bruschette di nonna Gina”..."," Sono bruschette con pomodoro, basilico, olio e un po’ di pecorino… squisite!","Sì, immagino... Però io vorrei anche un primo. ","Leggo “fusilli a modo nostro”: simpatico! Chissà cosa ci mettono.","E beh, basta chiedere... Cameriere!","Prego signori, avete deciso?","Sì, ma prima una domanda: cosa c’è nei fusilli “a modo vostro”?","“A modo nostro”, sì. Dunque, sono fusilli in salsa di pomodoro con capperi, olive, un po’ di mozzarella messa in salsa calda, peperoncino e salsiccia.","Uhm, sembra buono! Però per me senza peperoncino. Non amo i piatti troppo piccanti.","Anche io li prendo. Per me vanno bene, così, buoni!","... Anzi, facciamo anche senza salsiccia. Potete metterci invece un po’ di pancetta tagliata fine? ","E invece dei capperi, un po’ di basilico. Ah, e senza mozzarella. E ora che ci penso, neanche le olive, grazie. ","Sì, signora.","Sì, ma così non sono più a “modo loro”, sono “a modo tuo”. ","Allora ordina dei fusilli al pomodoro e basilico e fai prima!","Sei sempre il solito! Ma che vuoi? Ho chiesto il tuo parere?","Scusa, scusa! Caratterino!","E per secondo?","Ah no, scusi, prima ho dimenticato di dire che vogliamo anche le bruschette come antipasto."," E secondo, non so...","No no, io salto il secondo. Per me un’insalata mista.","No, io prendo le scaloppine al limone. E patate come contorno.","Scusi, che cosa c’è nell’insalata mista?","Beh, lattughe, pomodori, cetrioli...","Ecco, per me senza cetrioli.","Sì, anche senza pomodori e pochissima lattuga. In pratica, un piatto vuoto.","Lorenzo!! Sei impossibile, lo sai?","Io, impossibile??"]
trans3 = ["Доброе утро! Два да! Да, на имя  ... стол там?"," Ну, мило, не так ли? Да, да. Ты часто тут бываешь? ","Ну, с детства с родителями, а теперь с друзьями. ","Мне всегда нравилась атмосфера.","Да и потом... тут вкусно пахнет!","Да(иначе).... Ну, я не знаю как ты, но я голоден!","О, сколько хорошего! Так, посмотрим... Что ты мне посоветуешь?","А, здесь вкусные закуски. Читай здесь: брускетта от бабушки джино”.."," Это брускетта с помидорами, базиликом, маслом и немного сыра ... вкусно!","Да, полагаю... Но я тоже хочу первое. ","Я читаю фузилли нашим рецептом»: мило! Как знать что они нам положат.","Ну, просто спросите... Официант!","Пожалуйста, господа, вы решили?","Да, но сначала вопрос: что в фузилли нашим рецептом?","нашим рецептом, да. Итак, я фузилли в томатном соусе с каперсами, оливками, немного сыр моцарелла положенный в горячий соус, перец и колбаса.","Звучит неплохо! Но для меня без чили. Я не люблю блюда слишком острые.","Я тоже их беру. Для меня все хорошо, так, хорошо!","... Даже без колбасы. Можете ли вы положить немного бекона на конец? ","А вместо каперсов немного базилика. А, и без моцареллы. И теперь, когда я думаю об этом, оливки тоже, спасибо.","Да, мэм.","Да, но они больше не наш рецепт, они твой рецепт. ","Тогда закажите фузилли с томатным соусом и базиликом и сделайте это раньше!","Ты всегда обычный! Чего ты хочешь? Я спрашивала твое мнение?","Прости, прости! Ну и характер!","А на второе?","О, Нет, извините, я забыл сказать, что мы также хотим чеснок как закуска. ","А во-вторых, я не знаю...","Нет, нет, я  без второй. Для меня смешанный салат.","Нет, я возьму лимонные гребешки. И картофель в качестве гарнира.","Простите, что в смешанном салате?","Ну, салат-латук, помидоры, огурцы...","Вот, для меня без огурцов.","Да, даже без помидоров и очень мало листьев салата. На практике пустой тарелкой.","Лоренцо!! Ты невозможен.","Я невозможный??" ]

text4 = ["Lorenzo, sono Gianna. Che piano?","Primo. L’ascensore è in fondo a destra.","Va bene. Grazie!","Ciao. Come stai?","Bene!","Problemi per arrivare?","No no, nessun problema: l’autobus ferma proprio qui vicino. Ehi, ma è carina!","Grazie. Non è in centro, ma almeno è tranquilla.","Non è nemmeno troppo piccolo, come appartamento.","Sono 60 metri quadri. Per una persona sola vanno benissimo. Questo è il soggiorno","Carino!","E lì c’è la camera da letto…","Che confusione! Ma non metti mai in ordine?","Lo sai, sono disordinato. E qui è il bagno…","Che bella doccia grande che hai, che bello!","… Ed ecco la cucina.","Comoda, pratica! C’è tutto quello che serve. Proprio bella la tua casa!","E c’è anche un bel balcone, come vedi. Senti, vuoi bere qualcosa? Posso prepararti un caffè…","Sì, volentieri! Ma con questo bel tempo perché non usciamo? Beviamo qualcosa fuori! Che ne dici?","Buona idea. E c’è anche un bel bar proprio qui vicino.","Perfetto! Andiamo allora!","Ah, senti, però non posso restare molto tempo. Sai, tra due settimane ho un esame e devo ancora studiare un libro di 300 pagine!","D’accordo, non c’è problema. Tanto io devo andare in palestra, tra poco.","Che ore sono adesso…?","Quattro e mezza.","Io faccio le quattro e quaranta. Comunque beviamo qualcosa e tra mezz’ora sei di nuovo a casa!","Facciamo anche un’ora! Prego!"]
trans4 = ["Лоренцо я жиана. какой этаж?","Первый. Лифт в глубине справа.","Хорошо.спасибо ","Привет. Как дела?","Хорошо!","Проблемы по пути?","Нет нет, никаких проблем. Автобус остановился прямо рядом с остановкой. Но тут мило.","Спасибо. Не в центре но хотя бы спокойно.","Не слишком маленькое для аппартамтов.","60 метров квадратных. Для одного чловека подходит замечательно. Это гостиная.","Мило.","И вот спальня.","Какой бардак. Ты никогда не убираешься?","Ты знаешь, я не собранный. А вот ванна.","Какой большой душ! Какой красивый!","А вот кухня.","Компактная удобная! Тут есть всё что нужно. Хороший у тебя дом!","И вот ещё красивый балкон, как видишь. Слушай, хочешь выпить чего-нибудь? Могу приготовить кофе.","Да, с удовольствием! Но с такой прекрасной погодой почему бы не выйти? Выпить что-нибудь наружи. Что скажешь?","Чудесная идея. И тут чудесный бар тут рядом.","Прекрасно! Пошли тогда!","Слушай, я не могу оставаться долго. Знаешь у меня через 2 недели экзамен и мне надо ещё выучить книгу в 300 страниц.","Хорошо, это не проблема. В  мне надо пойти в зал через немного.","Cколько сейчас времени?","4 с половиной","А у меня 4 15. в любом случае выпьем чтонибудь и через пол часа ты снова дома","Давай час! Пожалуйста!"]

text5 = ["Da quando siamo all’università, Cristiana, Anna ed io non ci vediamo molto spesso. ","Ma quando eravamo al liceo, era tutta un’altra storia.","Infatti ci vedevamo tutti i giorni perché frequentavamo lo stesso liceo, anche se in classi diverse. ","Io partivo da casa alle sette, Cristiana alle sei e mezza (perché abitava molto lontano dalla scuola), Anna, invece, alle sette e venti (la sua casa si trovava a due passi dal liceo). ","Ci incontravamo tutti i giorni alle 7 e mezza alla fermata dell’autobus. ","Io e Cristiana eravamo sempre belle sveglie, Anna invece aveva sempre sonno, e raramente arrivava puntuale al nostro appuntamento. ","Dovevamo sempre aspettarla almeno cinque minuti. ","Le lezioni cominciavano alle otto, perciò avevamo sempre un po’ di tempo libero prima della “tortura”: di solito chiacchieravamo e ripassavamo qualcosa; ognuna aveva la sua materia preferita: io ero più forte in storia dell’arte e in latino, Cristiana in greco e in matematica.  ","Anna...lei arrivava appena alla sufficienza in tutto!","Non ricordo bene che cosa facevamo in classe, so solo che in generale mi annoiavo molto e aspettavo con ansia l’ora della ricreazione, cioé le dieci e mezza. ","A quell’ora uscivamo tutti dalla classe, compravamo qualcosa da mangiare e cercavamo di rilassarci. ","Io andavo a raggiungere Anna e Cristiana nella loro classe, e poi ci univamo ai nostri amici delle altre classi. ","Mi ricordo che avevamo tutti i giorni lezione di greco, latino e italiano; due volte la settimana c’erano matematica e fisica, una volta la settimana educazione fisica. ","Studiavamo anche chimica, biologia e inglese, ma non ricordo quando, perché non mi interessavano molto. ","Comunque all’una suonava la campanella e tutti uscivano di gran fretta. ","Io, Cristiana ed Anna ci ritrovavamo all’uscita e assieme facevamo programmi per il pomeriggio.","Al pomeriggio avevamo sempre molti compiti, studiavo sempre dalle tre alle sei. ","Una volta alla settimana io, Cristiana e Anna studiavamo assieme, anche se non combinavamo niente, guardavamo la televisione, giocavamo con il computer, ascoltavamo la musica. "]
trans5 = ["C тех пор как мы учимся в университете, кристина, анна и я не видимся очень часто. ","Но когда мы были в школе, это было совсем другая история ","В самом деле мы виделись каждый день потому что учились в одном лицее, хотя в разных классах. ","Я выходила из дома в 7, кристина в 6 30(потому что жила очень далеко от школы) анна наоборот в 7 20(её дом был в двух шагах от лицея) ","Встречались каждый день в 7 30 на автобусной остановке ."," я и кристина всегда хорошо вставали, анна наоборот всё время была сонная, и редко приходила вовремя на наши встречи. ","Нам нужно было обычно ждать 5 минут. ","Уроки наичинались в 8, потому у нас обычно было немного времени свободного перед муками,обычно болтали и повторяли что то. Каждая имела свой любимый предмет, я была сильнее в истории искусств и в итальняском, кристина в греческом и математике, ","анна, она ч трудом получала тройки по всему.","Я не помню хорошо вещи которые происходили в классе, знаю только что в целом я скучала сильно и с нетерпением ждала часа перемены, и вообще 10 30. ","В этот час все выходили из классов , покупали что то поесть и пытались отдохнуть.","я шла встретиться с анной и кристиной в их класс и потом собирались наши друзья из других классов. ","Я помню каждый день был греческий латынь и итальянский, 2 раза в неделю была математика и физика, один раз в неделю физкультура. ","Ещё учили химию биологию и английский,но я не помню сколько, потому что мне не было очень интересно. ","В любом случае в час звенел звонок и все выходили в большой спешке. ","Я кристина и анна встречались около выхода ии вместе делали планы на вторую половину дня. ","Во второй половине дгя обычно имели много дз, учились обычно с 3 до 6. ","раз в неделю я кристина и анна занимались вместе, однако не решали ничего, смотрели телевизор, ели конфеты и чипсы,играли в компьютер, слушали музыку."]

text6 = ["  Non segni mai le cose che devi comprare?","No, perché? ...Le ricordo. Ecco il caffè! Lo prendi anche tu?","Per forza! Sergio ne beve tre-quattro al giorno.","   Io compro Lavazza qualità oro...","   Io, invece, prendo Illy  Sergio lo preferisce alle altre marche. Perché non lo provi?","   Va be’, lo provo... Dunque... i biscotti...","   Io compro sempre questi del Mulino Bianco  a Sergio piacciono tanto! E poi questa confezione è anche economica.","   Ok, mi hai convinta, li provo anch’io. Ah, ecco le mele che vuoi comprare.","   Però Sergio le mele verdi non le mangia, le vuole rosse. Non importa, compro delle banane.","   Vuoi anche il formaggio, vero?","   Sì, prendo due etti di Parmigiano Reggiano.","   Io, in genere, prendo il Grana Padano  costa di meno ed è buono lo stesso.","   Lo so che costa di meno, ma Sergio mangia solo il meglio.","   Certo che lo tratti bene il tuo Sergio, eh???"]
trans6 = ["Не записываешь никогда вещи которые надо купить?","Нет зачем? Помню их, вот кофе! Ты тоже его возьмёшь?","Конечно! Серджио пьёт его три четыри раза в день","Я куплю лаваза качество золотое","Я наоборот возьму илли серджио предпочитает его другим маркам. Почему не попробуешь его?","Хорошо, я попробу, и так, печенье","Я обычно покупаю эти от мулина бьянко серджио их очень любит! И более эта упаковка ещё и экономная","Ок ты убедила меня, я тоже их попробую. О вот яблоки которые ты хотела купить","Однако серджио зелёные яблоки не есть их, он хочет красные. Не важно, куплю эти бананы","Ты хотел ещё сыр, правда?","Да, возьму 2 сотни гр пармиджано риджано","Я обычно беру гранде подано стоит меньше и скучный так же","Знаю что стоит меньше но серджио ест только лучшее","Конечно былуешь ты своего серджио?"]

text6 = ["mi piace molto lo sport gioco a calcio e la domenica a volte faccio un giro in collina com la mia moto","amo molto leggerr e andare a teatro ma mi piace anche fare passegiato in spiaggia con il mio cane un belissimo pastore tedesco di nome rex" ,"sono italiano di origina indiana","faccio l'opperaio in una famosa fabbrica di automobili di torino","guardo la tv su un comoda poltrone","faciamo una gita in montagna co qualche amico","adoro la musca e so abbastanza bene suonare la chitarra"]
trans6 = ["очень нравится спорт  играю в футболл и по вс иногда прогуливаюсь по холмам со своим мотоциклом","люблю  очень читать и ходить в театр но ещё мне нравится прогуливаться по пляжу со своей собакой чудесной немецкой породы по имени рекс","я итальянска  родом из индии","работю оператором на известной выбрики по производству автомобилей в торино","смотрю телевизор на удобном крселе","совершаю прогулку в горы с каким нибудь другом","обожаю музыку и умею играть очень хорошо на гитаре"]

text71 = ["LORENZO Allora, hai deciso che film andiamo a vedere?","GIANNA Beh, ci sono due o tre film interessanti.","LORENZO Per esempio?","GIANNA Beh, è uscito l’ultimo di Nanni Moretti. Di solito mi piacciono i suoi film.","LORENZ Sì, ma non volevi andare a vedere qualcosa di allegro? Ho sentito che è bello, ma un po’malinconico.","GIANNA Hai ragione, meglio qualcosa di più vivace.","LORENZO Se non sbaglio, oggi esce l’ultimo con Will Smith!","GIANNA  E no, caro mio, stavolta non ci casco! L’ultima volta che siamo andati a vedere un film con lui per poco non svenivo!","LORENZO Ma dai, per un po’ di sangue… E poi c’era anche una parte romantica.","GIANNA Non è vero! Di romantico non c’era proprio niente!","LORENZO D’accordo, d’accordo! Come non detto. E allora proponi tu qualcosa.","GIANNA ","Allora, qui vedo che è uscito il film di Muccino che ha vinto tutti quei premi… Che dici? Muccino piace anche a te, no? Lo danno all’Odeon. ","LORENZO A che ora è il primo spettacolo?","GIANNA Alle sei e mezza. ","LORENZOTra venti minuti. Allora è meglio che ci sbrighiamo.","GIANNA Ok.","LORENZO Tieni.","GIANNA Grazie. Senti, prendiamo i pop corn? Da piccola, quando andavo al cinema con i miei, li prendevo sempre!","LORENZO D’accordo. Se li prendevi da piccola... Prendiamo uno di questi...","GIANNA Allora, bello no? Non credevo così.","LORENZO Bello, bello… Poi con tutti quei panorami di Firenze... Bello.","GIANNA Ma che Firenze? Era Perugia!","LORENZO Ah, giusto. Perugia, sì. Ma perché poi alla fine lui scappa con la cugina?","GIANNA Non era la cugina, era un’amica! E non sono scappati.","LORENZO Ma non era la figlia del fratello, il fratello che viveva a Milano…no?","GIANNA Ma che dici? Quello non era il fratello! Il fratello abitava con quella donna che faceva l’avvocato. Lorenzo, ma dormivi o hai visto il film?","LORENZ Mmh, effettivamente, devo essermi addormentato a metà del film..."]
trans71 = ["Лоренцо Итак, ты решил, какой фильм мы будем смотреть?","Джанна Ну, есть два или три интересных фильма.","Лоренцо Например?","Джанна Ну, вышел последний от Нанни Моретти. Обычно мне нравятся его фильмы.","Лоренцо Да, но разве ты не хотел пойти посмотреть что-нибудь веселое? Я слышал, что это красиво, но немного меланхоличный.","Джанна Ты прав, лучше что-нибудь более живое.","Лоренцо Если я не ошибаюсь, сегодня последний выходит с Уиллом Смитом!","Джанна И нет, дорогой мой, на этот раз я не поведусь! В последний раз мы пошли смотреть фильм с ним для я чуть в обморок не упала!","Лоренцо Да ладно, немного крови ... а потом была и романтическая часть.","Джанна Это неправда! Ничего романтического не было!","Лоренцо Ладно, ладно! Не за что. Тогда предложи что-нибудь.","Джаннаf      ","Так вот, я вижу, что вышел фильм Кучино, который выиграл все эти награды ... что скажешь? Кучинотебе тоже нравится, да? Показывают  его в Одеону.","Лоренцо Во сколько первый сеанс?","Джанна В половине шестого.","Лоренцо Через 20 минут. Тогда нам лучше поторопиться.","Джанна Хорошо.","Лоренцо подожди","Джанна Благодарю. Слушай, мы берем попкорн? В детстве, когда я ходила в кино с родителями, я брала их всегда! ","Лоренцо Хорошо. Если бы ты взяла их, когда была маленькой... Давайте возьмем один из них...","Джанна Ну что, красиво нет  ? Я так не думал."," Лоренцо Красиво, красиво ... потом со всеми этими видами Флоренции... Красивый.","Джанна Что за Флоренция? Это Был Перуджа!","Лоренцо Точно. Перуджа, да. Но почему он в конце концов убегает с кузиной?","Джанна Это была не Кузина, а подруга! И они не сбежали.","Лоренцо Но она не была дочерью брата, брата, который жил в Milano...no?","Джанна О чем ты говоришь? Это был не брат! Его брат жил с той женщиной, которая была адвокатом. Лоренцо, ты спал или смотрел фильм?","Лоренцо МММ, на самом деле, я, должно быть, заснул на полпути к фильму..."]

text8 =["- Ciao Lidia, come va?","- Non c’è male, grazie. E tu?","- Abbastanza bene. Allora... come hai passato il fine settimana?","- Mah, niente di speciale, le solite cose.","- E dai, racconta.","- Dunque... sabato sono andata con Gianna in centro... a fare spese. Poi abbiamo bevuto un caffè all’Antico Caffè Greco e verso le 9 siamo andate a mangiare una pizza con degli amici.","- E ieri?","- Ieri, niente, sono andata da una mia collega. Abbiamo cenato e abbiamo guardato un film in televisione. Be’... non è stato tanto divertente devo dire. Comunque, sono rimasta fino a mezzanotte. E tu, cosa hai fatto di bello? Sei uscito con i ragazzi alla fine?","- Sì... sabato sera siamo andati in discoteca. Abbiamo ballato un sacco e siamo tornati dopo le tre!","- Allora, ieri non sei uscito, immagino...","- Invece, sì! Nel pomeriggio sono andato da Paola a guardare la tv. Verso le otto, però, lei ha avuto l’idea di andare al cinema e... così siamo usciti in gran fretta. Pensa che siamo entrati in sala un minuto prima dell’inizio del film!","- Dai! Un fine settimana intenso, insomma","- Beh, sì! Ma anche divertente...!"]
trans8 = ["- Привет, Лидия, как дела?","- Неплохо, спасибо. А ты?","- Неплохо. Тогда... как ты провел выходные?","- Ничего особенного, обычные вещи.","- Да ладно, рассказывай.","- Итак... в субботу я ездила с Джанной в центр города... за покупками. Затем мы выпили кофе в древнегреческом кафе и около 9 часов пошли есть пиццу с друзьями.","- А вчера?","- Вчера, ничего, я ходила к коллеге. Мы ужинали и смотрели фильм по телевизору. Ну... это было не так весело, я должен сказать. Во всяком случае, я пробыла до полуночи. А ты, что хорошего сделал? Ты встречался с ребятами в конце?","- Да... в субботу вечером мы пошли на дискотеку. Мы много танцевали и вернулись после трех!","- Значит, вчера ты не выходил, я полагаю...","- Нет, да! Днем я пошел к Паоле смотреть телевизор. Около восьми, однако, у нее появилась идея пойти в кино И... поэтому мы вышли очень быстро. Он думает, что мы вошли в зал за минуту до начала фильма!","- Давай! Напряженные выходные, короче","- Ну да! Но и смешно...!"]

text9 =["Riccardo rientra a casa all'ora di cena e parla con sua moglie che prepara da mangiare.","Riccardo: Ciao Lia, eccomi qua. È pronta la cena?","Lia: Quasi pronta, Riccardo. Ti sei ricordato di procurare i biglietti per lo spettacolo di questa sera? Il palco l'avevo già prenotato io.","Riccardo: Ce li ho, ce li ho! Li ho fatti prendere dalla mia segretaria.","Lia: Ho saputo da Giovanna che c’era molta gente al botteghino; li ha comprati poi?","Riccardo: Sì, è riuscita a farli, anche se ha dovuto fare la fila. Ma dove li ho messi? Ah, eccoli qui.","Lia: Quanti ne ha fatti?","Riccardo: Ne ha comprati quattro: due per noi e due per i signori Santini.","Lia: Come? I Santini vengono con noi?","Riccardo: Sicuro. La volta scorsa, quando li abbiamo incontrati al tennis club dove ci avevano invitato a cena, avevano espresso il desiderio di vedere l'ultima commedia di Eduardo De Filippo; così io li hoinvitati questa sera nel nostro palco.","Lia: Ma Riccardo, ti ho detto tante volte che lei, non la sopporto; mi ha incontrato spesso per la strada e non mi ha mai salutata. ","Riccardo: E che ci posso fare? Tu non sopporti lei, io non sopporto lui, ma dobbiamo restituire la cortesia. Su, su, dobbiamo cenare in fretta. Se ci mettiamo a discutere faremo tardi e non ci faranno entrare."]
trans9 =["Риккардо возвращается домой во время ужина и разговаривает с женой, которая готовит еду.","Привет, Лия, вот и я. Ужин готов?","Лия: почти готова, Ричард. Ты не забыл купить билеты на сегодняшнее шоу? Я уже заказал сцену.","Риккардо: У меня есть, у меня есть! Я заставила их забрать у моей секретарши.","Лия: я слышала от Жанны, что в кассе много народу; вы их потом купили?","Риккардо: Да, ей удалось их сделать, хотя ей пришлось стоять в очереди. Но куда я их положил? А, вот они.","Лия: сколько он сделал?","Риккардо: он купил четыре: два для нас и два для сеньоров Сантини.","Лия: Как? Сантини с нами?","Ричард: Конечно. В прошлый раз, когда мы встретились с ними в теннисном клубе, где они пригласили нас на ужин, они выразили желание посмотреть последнюю комедию Эдуардо де Филиппо; так что я их приглашены сегодня на нашу сцену.","Лия: но Ричард, я тебе столько раз говорил, что она, я ее терпеть не могу; она часто встречала меня на улице и никогда не здоровалась со мной.","Риккардо: а что я могу с этим поделать? Ты терпеть не можешь ее, я терпеть не могу его, но мы должны вернуть вежливость. Давай, давай, нам нужно быстро поужинать. Если мы будем спорить, мы опоздаем, и нас не пустят."]

text10 =["Gigi, ladro ben noto alla polizia, dopo cinque anni di prigione, è in libertà. Ma ora si trova al commissariato di polizia perché su lui pesa il sospetto di un nuovo furto. ","Commissario: Siccome cinque anni di galera non ti sono bastati, ti sei rimesso al lavoro. Adesso, se non vuoi tornare al fresco per altri cinque anni, mi racconti per filo e per segno quello che è successo sabato notte in casa della marchesa.","Gigi: E va bene, Commissario, Le dirò tutto. Sabato, a mezzanotte sono entrato nella villa della marchesa.","Commissario: Chi sono stati i tuoi complici? Fuori i nomi!","Gigi: Su questo non mi caverà una parola di bocca.","Commissario:  Senti, amico, il colpo non puoi averlo fatto da solo. Tì conviene “cantare”. Come hai trovato i complici?","Gigi: Me li ha forniti la Sdentata.","Commissario: Vedi che cominciamo ad andare d’accordo? Ah, te li ha trovati la Sdentata?! È tornata anche lei nel “giro”. E chi vi ha dato la pianta della villa?","Gigi No. Questo non posso proprio dirglielo.","Commissario: Ricominci?","Gigi: Ce l’ha fornita il maggiordomo.","Commissario: Chi l’avrebbe detto! Un servitore così fedele per tanti anni! E le chiavi della villa? E la combinazione della cassaforte?","Gigi: Ce le ha procurate... Commissario, non posso...","Commissario: Non fare storie! Chi ve le ha date?","Gigi: La cameriera personale della marchesa.","Commissario: Bene! Anche la cameriera! Adesso devi dirmi chi è entrato con te nella villa.","Gigi: Sono entrati con me il Lungo e lo Smilzo.","Commissario: Voi soli?","Gigi: Sì, il Muto ci aspettava in macchina e il Tappo faceva da palo.","Commissario: E con i cani che ancora dormono, come avete fatto?","Gigi: Facile. Avevamo lo spray soporifero. Glielabbiamo spruzzato sul muso... Gliene abbiamo spruzzato tanto."]
trans10 =["Джиджи, хорошо известный в полиции вор, после пяти лет тюрьмы, находится на свободе. Но сейчас он находится в полицейском комиссариате, потому что на нем лежит подозрение в новой краже.","Комиссар: Так как пяти лет тюрьмы тебе не хватило, ты вернулся к работе. А теперь, если ты не хочешь возвращаться в прохладу еще на пять лет, расскажи мне по нитям и знакам, что произошло в субботу вечером в доме маркизы. ","Гиги: Ладно, комиссар, я вам все расскажу. В субботу, в полночь, я вошел в особняк маркизы.",": Кто твои сообщники? Убирайте имена!","Гиги:Я ни слова не скажу об этом.","Комиссар:Слушай, чувак, ты не можешь сделать это сам. Тебе лучше спеть Как ты нашел сообщников?","Гиги:Беззубый дал их мне.","Комиссар:Видишь, мы начинаем ладить? А, беззубая нашла?! Она тоже вернулась в круг. И кто дал вам план виллы?","ГигиНет. Я не могу вам этого сказать.","Комиссар:Начнешь снова?","ГигиДворецкий предоставил его нам.","Комиссар:Кто бы мог подумать! Такой верный слуга столько лет! А ключи от виллы? А как насчет комбинации сейфа?","Гиги:Он достал их... Комиссар, я не могу...","Комиссар:Не суетись! Кто вам их дал?","Гиги:Личная горничная маркизы.","Комиссар:Хорошо! Даже официантка! Теперь ты должен сказать мне, кто вошел с тобой в особняк.","Гиги:Они вошли вместе со мной длинный и улыбчивый.","Комиссар:Вы одни?","Гиги:Да, немой ждал нас в машине, а колпак стоял столбом.","Комиссар:А с собаками, которые все еще спят, как вы это сделали?","Гиги:Легкий. У нас был снотворный спрей. Мы плеснули ему в морду... Мы ему столько брызгали."]

text11 = ["Oggi vado in un negozio di piante e compro un cactus.","E un bellissimo cactus: è alto due metri, è tutto verde e ha molte spine.","Lo porto con me in autobus: gli altri passeggeri non sembrano moltocontenti."," Finalmente arriviamo a casa: comincio a cercare un posto dovemetterlo."," Prima voglio metterlo in soggiorno, ma là c’è sempre latelevisione accesa, e forse questo al cactus non piace. ","Allora lo portoin cucina, dalla mamma."," Lei non è molto contenta del mio acquisto. ","Midice di portarlo via: secondo lei in cucina non c’è posto, il cactus ladisturba e lei deve preparare la cena. ","Nel corridoio non può stareperché è troppo stretto."," Forse può stare in bagno, dentro la vasca, main questo momento mia sorella sta facendo la doccia e la porta è chiusaProvo abussare, ma lei non apre. ","E’ strano: perché non vuole fare ladoccia insieme al mio povero cactus?"," Lo porto nella camera del nonno."," Il nonno è molto contento della nostra visita: nessuno entra mai nella suastanza."," Da lui c’è un grande disordine: le scarpe sono sul tavolo, ivestiti sono sul comodino, i libri sono nell’armadio e le medicine sonosul tappeto. ","Il nonno saluta il cactus: non capisce che è una pianta, enon una persona. ","Si mette subito a conversare con lui; gli chiede seconosce il lago di Garda, e poi comincia a descrivere i grossi pesci,lunghi due metri, che una volta c’erano nel lago di Garda. ","Dopo un po’capisco che il mio cactus ha bisogno di un posto più tranquillo. ","Loporto via, mentre il nonno continua a parlare da solo. ","Mia madresuggerisce di mettere il cactus sul balcone, ma questo non è possibileè una pianta tropicale, e sul balcone fa troppo freddo per lui. ","Alloralo porto nella camera dei miei genitori: è il posto ideale per lui.","Purtròppo, quando più tardi papà toma dall’ufficio e vede il cactus, cheoccupa metà della stanza con i suoi lunghi rami, si arrabbia e mi ordinadi riportarlo al negozio. ","Ma ormai sono le otto, il negozio è giàchiuso. ","Così alla fine ci*mettiamo d’accordo e decidiamo di mettere ilcactus nell’ingresso: lo useremo come attaccapanni."]
trans11 = ["Сегодня я иду в растительный магазин и покупаю кактус.","Это красивый кактус: он высотой два метра, он весь зеленый и имеетмного шипов. ","Я беру его с собой на автобусе: другие пассажиры,похоже, не очень довольны."," Наконец мы добираемся до дома: я начинаюискать место, где бы его разместить."," Сначала я хочу поместить его вгостиную, но там всегда телевизор включен, и, возможно, это кактусу ненравится Тогда я отведу его на кухню, к маме."," Вы не очень довольны моейпокупкой."," Она велит мне увести его: по ее словам, на кухне нет места,кактус беспокоит ее, и она должна приготовить ужин."," В коридоре нельзястоять, потому что он слишком узок."," Может быть, она может остаться вванной, в ванной, но сейчас моя сестра принимает душ, и дверь закрыта."," Япытаюсь оттолкнуть ее, но она не открывает."," Странно: почему она не хочетпринять душ вместе с моим бедным кактусом?"," Я отведу его в комнату деда.","Дедушка очень доволен нашим визитом: никто никогда не входит в егокомнату."," От него большой беспорядок: обувь на столе, одежда на тумбочке,книги в шкафу, а лекарства-на ковре."," Дед здоровается с кактусом: он непонимает, что это растение, а не человек."," Она сразу же начинает с нимразговаривать; спрашивает, знает ли он озеро Гарда, а затем начинаетописывать большие рыбы, длиной в два метра, которые когда-то были возере Гарда. ","Через некоторое время я понимаю, что моему кактусу нужноболее спокойное место."," Я забираю его, а дедушка продолжает говорить сам с собой"," Мама предлагает поставить Кактус на балкон, но это невозможно: это тропическо растение, а на балконе для него слишком холодно. ","Тогда я отведу его в комнату моих родителей-это идеальное место для него.","К сожалению, когда позже папа Тома выходит из кабинета и видит кактус, занимающий половину комнаты своими длинными ветвями, он сердится и приказывает мне вернуть его в магазин.","Но уже восемь часов, магазин уже закрыт."," Итак, в конце концов мы*соглашаемся и решаем поставить кактус в подъезде: мы будем использовать его в качестве вешалки."]

bl = [" Se ho una lezione alla mattina e una al pomeriggio, cosa che succede molto spesso,rimango all’università: studio, navigo su Internet, passo un po’ di tempo con i miei amici. ","Ogni tanto mi capita di non andare ad unalezione a causa del lavoro: mi dispiace sempre molto perdere le lezioni,ma mi dispiace ancora di più non vedere i bambini!","Torno a casa versole sette o le otto, e a quell’ora ci riuniamo tutti per cena. "," Mi èsempre piaciuta l’atmosfera.","... Anzi, facciamo anche senza salsiccia.Potete metterci invece un po’ di pancetta tagliata fine? ","Ah no,scusi, prima ho dimenticato di dire che vogliamo anche le bruschettecome antipasto.","A quell’ora uscivamo tutti dalla classe, compravamoqualcosa da mangiare e cercavamo di rilassarci. ","Io andavo araggiungere Anna e Cristiana nella loro classe, e poi ci univamo ainostri amici delle altre classi. ","Io, Cristiana ed Anna ci ritrovavamoall’uscita e assieme facevamo programmi per il pomeriggio."]
bt = ["Еслиу меня занятия утром и днем, что бывает очень часто, я остаюсь вуниверситете: учусь, сижу в Интернете, провожу время с моими друзьями.","Время от времени я не собираюсь идти на урок из-за работы: я всегдаочень сожалею о том, чтобы пропустить уроки,но я сожалею еще больше невижу детей!","Я прихожу домой около семи или восьми, и в тот час мы всесобираемся вместе на ужин.","Мне всегда нравилась атмосфера."," ... Дажебез колбасы. Можете ли вы положить немного бекона на конец? ","О, Нет,извините, я забыл сказать, что мы также хотим чеснок как закуска","Вэтот час все выходили из классов , покупали что то поесть и пыталисьотдохнуть.","я шла встретиться с анной и кристиной в их класс и потомсобирались наши друзья из других классов. ","Я кристина и аннавстречались около выхода ии вместе делали планы на вторую половину дня."]

lat = ["praesens act pass","imperfectum act pass","futurum1 act pass","perfectum act pass","plusquamperfectum act pass","futurum2 act pass"]
latt = ["o (i 3a)s (i 3a)t (i 3a)mus (i 3a)tis (u)nt, or (e 3a)ris (i 3a)tur (i 3a)mur (i 3a)mini (u)ntur","(e)ba + m s t mus tis nt, (e)ba + r ris tur mur mini ntur", "b(1,2) + o i(e)s i(e)t i(e)mus i(e)tis u(e)nt, b(1,2) + or eris i(e)tur i(e)mur i(e)mini i(e)ntur","i isti it imus istis erunt, sum es est sumus estis sunt + us a um i ae a", "era+ m s t mus tis nt, eram aras erat eramus eratis erant + us a um i ae a", "eri + o s t mus tis nt, ero eris erit erimus eritis erunt + us a um i ae a"]
print("0 - латынь, 1 - про кино диалог, 2 - про день диалог, 3 - про поход в рестиоран, 7-che film andiamo a vedere, 8-come hai passato")
n_n = [len(lat),len(text1),len(text2),len(text3),len(text4),len(text5),len(text6),len(text71),len(text8),len(text9)]


for i in range(len(trans11)):
    print(text11[i])
    print(trans11[i])


while True:
    n = int(input())
    br = 0
    if n == 0:
        while br == 0:
            a = random.randint(0,n_n[n]-1)
            print(lat[a])
            if input() == "ex":
                br = 1

            print(latt[a])




    if n == 1:
        while br == 0:
            a = random.randint(0,n_n[n]-1)
            print(trans1[a])
            if input() == "ex":
                br = 1
            print(text1[a])



    if n == 2:
        while br ==0:
            a = random.randint(0,n_n[n]-1)
            print(trans2[a])
            if input() == "ex":
                br = 1
            print(text2[a])

    if n == 7:
        while br ==0:
            a = random.randint(0,n_n[n]-1)
            print(trans71[a])
            if input() == "ex":
                br = 1
            print(text71[a])

    if n == 8:
        while br ==0:
            a = random.randint(0,n_n[n]-1)
            print(trans8[a])
            if input() == "ex":
                br = 1
            print(text8[a])



    if n == 3:
        while  br ==0:
            a = random.randint(0,n_n[n]-1)
            print(trans3[a])
            if input() == "ex":
                br = 1
            print(text3[a])



    if n == 4:
        while br == 0:
            a = random.randint(0,n_n[n]-1)
            print(trans4[a])
            if input() == "ex":
                br = 1
            print(text4[a])



    if n == 5:
        while br == 0:
            a = random.randint(0,n_n[n]-1)
            print(trans5[a])
            if input() == "ex":
                br = 1
            print(text5[a])



    if n == 6:
        while br == 0:
            a = random.randint(0,n_n[n]-1)
            print(trans6[a])
            if input() == "ex":
                br = 1
            print(text6[a])



    if n == 9:
        while br == 0:
            a = random.randint(0,n_n[n]-1)
            print(trans9[a])
            if input() == "ex":
                br = 1
            print(text9[a])

    if n == 10:
        while br == 0:
            a = random.randint(0,len(text10))
            print(trans10[a])
            if input() == "ex":
                br = 1
            print(text10[a])


    if n == 3_1:
        while br == 0:
            for i in range(n_n[3]):
                print(trans9[i])
                if input() == "ex":
                    br = 1
                print(text9[i])



    if n == 2_1:
        while br == 0:
            for i in range(n_n[2]):
                print(trans2[i])
                if input() == "ex":
                    br = 1
                print(text2[i])
    if n == 51:
         while br == 0:
            for i in range(n_n[5]):
                print(trans5[i])
                if input() == "ex":
                    br = 1
                print(text5[i])

    if n == 6_1:
         while br == 0:
            for i in range(len(text6)):
                print(trans6[i])
                if input() == "ex":
                    br = 1
                print(text6[i])

    if n == 7_1:
         while br == 0:
            for i in range(17, len(text71)):
                print(trans71[i])
                print(i)
                if input() == "ex":
                    br = 1
                print(text71[i])


    if n == 8_1:
         while br == 0:
            for i in range(0,len(text8)):
                print(trans8[i])
                print(i)
                if input() == "ex":
                    br = 1
                print(text8[i])

    if n == 9_1:
         while br == 0:
            for i in range(len(text9)):
                print(trans9[i])
                if input() == "ex":
                    br = 1
                print(text9[i])


    if n == 10_1:
         while br == 0:
            for i in range(len(text9)):
                print(trans9[i])
                if input() == "ex":
                    br = 1
                print(text9[i])


    if n == 11_1:
         while br == 0:
            for i in range(len(text11)):
                print(trans11[i])
                if input() == "ex":
                    br = 1
                print(text11[i])
