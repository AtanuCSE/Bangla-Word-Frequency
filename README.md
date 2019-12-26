# Bangla-Word-Frequency
A simple project to get the line in Bangla language and count the number of time each word appeared. 
In short, Word frequency counter for Bangla Language.
Reading Bangla from File, Preprocessing (optional. eg. Punctuation removal), frequency count.

Input:
সে অবশ্য বেশির ভাগ সময় থামি পড়তেই ভালোবাসে। তবে বর্ষা এলেই সে নীল রঙের প্রাধান্যটা যেন একটু বেশিই দেয়, মাঝে মাঝে নীল শাড়ির সাথে খোঁপায় সাদাফুল গুজে ভিজতে যায় মাতামুহুরির জলে। শীতে আবার অন্য সাঁজ, এ সময় তাকে দেখলে যে কেও টুরিস্ট না বলার ভুল করবেনা। এসময় দূর দুরান্তের সব পাহাড়গুলোই থাকে তার পায়ের তলে, খুব ব্যস্ত সময় পার করে। পায়ে বুট জুতো, জিন্স সাথে টিশার্ট জ্যকেট আর মাথায় গোলাকার একখানা হ্যট। পিঠে ঝোলানো থাকে ট্র্যাভেল ব্যগ ও হাতে এখানা লাঠি সম্বল করে বেড়িয়ে পরে।
এখন অবশ্য তার কাজে কর্মে কিছুটা পরিবর্তন এসেছে। যে ছেলেটা তাকে প্রতিদিন জল তুলে দেয় তার নাম ইয়াঙ্গু, সে এ বছর তাদের বিজু উৎসবে নিমন্ত্রণ করেছিলো ওদের গাঁয়ে, শৈলও খুশি মনে নিমন্ত্রণ স্বীকার করেছিলো। সুর্যটা যখন মিরিঞ্জা পাহাড়ের ওপারে ঢুলে গেলো শৈলও তখন তৈরি হয়ে চলল উৎসবে যোগ দিতে।

Output with stop words:
সে = 3
সময় = 3
তার = 3
অবশ্য = 2
নীল = 2
দেয় = 2
মাঝে = 2
সাথে = 2
এ = 2
তাকে = 2
যে = 2
থাকে = 2
উৎসবে = 2
নিমন্ত্রণ = 2
শৈলও = 2
বেশির = 1
ভাগ = 1
থামি = 1
পড়তেই = 1
ভালোবাসে = 1
তবে = 1
বর্ষা = 1
এলেই = 1
রঙের = 1
প্রাধান্যটা = 1
যেন = 1
একটু = 1
বেশিই = 1
শাড়ির = 1
খোঁপায় = 1
সাদাফুল = 1
গুজে = 1
ভিজতে = 1
যায় = 1
মাতামুহুরির = 1
জলে। = 1
শীতে = 1
আবার = 1
অন্য = 1
সাঁজ = 1
দেখলে = 1
কেও = 1
টুরিস্ট = 1
না = 1
বলার = 1
ভুল = 1
করবেনা। = 1
এসময় = 1
দূর = 1
দুরান্তের = 1
সব = 1
পাহাড়গুলোই = 1
পায়ের = 1
তলে = 1
খুব = 1
ব্যস্ত = 1
পার = 1
করে = 1
পায়ে = 1
বুট = 1
জুতো = 1
জিন্স = 1
টিশার্ট = 1
জ্যকেট = 1
আর = 1
মাথায় = 1
গোলাকার = 1
একখানা = 1
হ্যট। = 1
পিঠে = 1
ঝোলানো = 1
ট্র্যাভেল = 1
ব্যগ = 1
ও = 1
হাতে = 1
এখানা = 1
লাঠি = 1
সম্বল = 1
করে = 1
বেড়িয়ে = 1
পরে। = 1
এখন = 1
কাজে = 1
কর্মে = 1
কিছুটা = 1
পরিবর্তন = 1
এসেছে = 1
ছেলেটা = 1
প্রতিদিন = 1
জল = 1
তুলে = 1
নাম = 1
ইয়াঙ্গু = 1
বছর = 1
তাদের = 1
বিজু = 1
করেছিলো = 1
ওদের = 1
গাঁয়ে = 1
খুশি = 1
মনে = 1
স্বীকার = 1
করেছিলো। = 1
সুর্যটা = 1
যখন = 1
মিরিঞ্জা = 1
পাহাড়ের = 1
ওপারে = 1
ঢুলে = 1
গেলো = 1
তখন = 1
তৈরি = 1
হয়ে = 1
চলল = 1
যোগ = 1
দিতে = 1

Output without Bangla Stop Words: (Stop words taken from ranks.nl)
সময় = 3
নীল = 2
দেয় = 2
মাঝে = 2
সাথে = 2
উৎসবে = 2
নিমন্ত্রণ = 2
শৈলও = 2
বেশির = 1
ভাগ = 1
থামি = 1
পড়তেই = 1
ভালোবাসে = 1
বর্ষা = 1
এলেই = 1
রঙের = 1
প্রাধান্যটা = 1
একটু = 1
বেশিই = 1
শাড়ির = 1
খোঁপায় = 1
সাদাফুল = 1
গুজে = 1
ভিজতে = 1
যায় = 1
মাতামুহুরির = 1
জলে। = 1
শীতে = 1
সাঁজ = 1
দেখলে = 1
কেও = 1
টুরিস্ট = 1
বলার = 1
ভুল = 1
করবেনা = 1
এসময় = 1
দূর = 1
দুরান্তের = 1
পাহাড়গুলোই = 1
পায়ের = 1
তলে = 1
ব্যস্ত = 1
পার = 1
করে। = 1
পায়ে = 1
বুট = 1
জুতো = 1
জিন্স = 1
টিশার্ট = 1
জ্যকেট = 1
মাথায় = 1
গোলাকার = 1
একখানা = 1
হ্যট = 1
পিঠে = 1
ঝোলানো = 1
ট্র্যাভেল = 1
ব্যগ = 1
হাতে = 1
এখানা = 1
লাঠি = 1
সম্বল = 1
বেড়িয়ে = 1
পরে = 1
কর্মে = 1
কিছুটা = 1
পরিবর্তন = 1
এসেছে = 1
ছেলেটা = 1
প্রতিদিন = 1
জল = 1
নাম = 1
ইয়াঙ্গু = 1
বছর = 1
বিজু = 1
করেছিলো = 1
গাঁয়ে = 1
খুশি = 1
মনে = 1
স্বীকার = 1
করেছিলো। = 1
সুর্যটা = 1
মিরিঞ্জা = 1
পাহাড়ের = 1
ওপারে = 1
ঢুলে = 1
গেলো = 1
তৈরি = 1
হয়ে = 1
চলল = 1
যোগ = 1
দিতে। = 1
