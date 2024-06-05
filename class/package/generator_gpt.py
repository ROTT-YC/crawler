import openai

CONTENT_GENERATOR = """
Your task: In the tone of a news report, rewrite an article in English with a length of over 600 words for the concept [2], while keeping the summary unchanged. Also, create a different title for this article compared to [1].
Format:
[1] = {}
[2] = [ {} ]

- Use English or translate into English!
- The article must be at least 600 words in length, please expand and present it completely.
- Follow the following structure: "/title: [1] \n /content: [2]"
- Ensure that the words 'author', 'compiled' do not appear in the article.
- Example:
/title: Taskin to miss Test series against New Zealand
/content: Taskin Ahmed, the Bangladesh pacer, said he will not be available for the upcoming two-match Test series against New Zealand as he is still recovering from a shoulder injury. Taskin said he will begin rehabilitation shortly and is hopeful of being fit ahead of the three T20Is that Bangladesh will play when they tour New Zealand later in December.This means Taskin will also miss the ODI leg of Bangladesh's tour of New Zealand which begins on December 17, a week after the second Test ends.Taskin had a tear to his shoulder during the World Cup, forcing him to miss a couple of matches. "I was playing with a tear in my shoulder and I couldn't find my best rhythm (in the World Cup)," said Taskin. "I will not be playing the Test series against New Zealand at home in the coming winter as I want to do start rehabilitation after taking some rest and hoping to be available for the T20Is against New Zealand that is scheduled after our home series against them," he said that suggest he would not be available for the three-match ODI series through which the series will get underway.Apart from Taskin, Bangladesh skipper Shakib Al Hasan will miss also the Test series against New Zealand due to fractured finger while Tamim Iqbal's availability is still in doubt. It is still unclear is he has recovered from a back injury and he also did not participate in the National Cricket League.The Bangladesh team returned home from Pune on Sunday after their World Cup campaign where they finished with only two wins out of nine matches. Taskin felt that the disturbance caused by the differences between Shakib and Tamim leading into the World Cup was not good for the team. "As a player, we didn't have any control over it (Shakib's problem with Tamim). Definitely, no disturbance is good for the team. It is better not to have any disturbances," said Taskin.Meanwhile, Taskin said the team will miss the services of fast bowling coach Allan Donald who stepped down from his position after the World Cup. "He (Donald) took care of our fast bowling exceptionally well. He always backed us regardless of our performance. He motivated us a lot. I enjoyed working with him. He is leaving us, but that's life. Every coach has a two or four-year span. I wish him for his future," he said.
"""

# Generate with <h2></h2>
CONTENT_GENERATOR_h2 = """
Your task: In the tone of a news report, rewrite an article in English with a length of over 600 words for the concept [2], while keeping the summary unchanged. Also, create a different title for this article compared to [1].
Format:
[1] = {}
[2] = [ {} ]

- Use English or translate into English!
- The article must be at least 600 words in length, please expand and present it completely.
- Follow the following structure: "/title: [1] \n /content: [2]"
- Ensure that the words 'author', 'compiled' do not appear in the article.
- The content must have section headings, which should be presented using <h2></h2> tags.
- Example:
/title: Claiming Lottery Winnings: A Guide to Your Lucky Jackpot
/content: Winning a prize in the lottery immediately qualifies you as one of the luckiest people in the world. Or maybe the strategic tips on how to win the lottery worked out for you. First, let us congratulate you! Once the first rush of happiness goes away, it is time to consider how to claim your prize. The rules for claiming rewards might vary from one game to another. Here is a detailed guide on how long it takes after winning the lottery to get the money!<h2>Understanding the Lottery Claim Process</h2>Lottery enthusiasts and dreamers all over the world participate in lotto games with the hope of hitting the jackpot. Among these games, the US Powerball stands out as a favorite, with millions playing globally and especially in the United States. While some try their luck with strategies like the lotto dominator, the first practical step after winning is understanding how to claim the prize.<h2>Know Your Deadline</h2>The deadlines to claim Powerball prizes differ across states, ranging from 90 days to a full year. This critical information is usually found on the back of the ticket, alongside the expiration date. Missing the deadline forfeits the win, emphasizing the importance of knowing the claim period for your particular state.<h2>Similarities with Mega Millions</h2>Similarly, the procedures for Mega Millions winners are much like those for Powerball, with both lotteries offering some of the most significant jackpots ever seen. One key distinction is Mega Millions tickets aren't available in Puerto Rico, which doesn't participate in this game.<h2>Conclusion</h2>In conclusion, winning the lottery is a dream come true for many, but it's essential to understand the steps and deadlines for claiming your prize. Whether you've won the Powerball or Mega Millions, knowing the rules can make a significant difference in ensuring you receive your jackpot winnings. Good luck, and may your lottery dreams come true!
"""

# Hindi
CONTENT_GENERATOR_HINDI = """
आपका काम: एक समाचार रिपोर्ट के धुन में, एक लेख को हिंदी में लिखें, जिसकी लंबाई 600 शब्द से अधिक हो, कॉन्सेप्ट [2] के लिए, हालांकि सारांश को बिना बदले रखें। इसके अलावा, इस लेख के लिए [1] के समान नाम बनाएं।
स्वरूप:
[1] = {}
[2] = [ {} ]

- हिंदी का उपयोग करें या हिंदी में अनुवाद करें! 
- लेख की लंबाई कम से कम 600 शब्द की होनी चाहिए, कृपया इसे विस्तारित करें और पूरी तरह से प्रस्तुत करें।
- निम्नलिखित संरचना का पालन करें: "/title: [1] \n /content: [2]"
- यह सुनिश्चित करें कि लेख में 'लेखक', 'संकलित' शब्द नहीं आते हैं।
- सामग्री के पास अनुभाग शीर्षक होने चाहिए, जिन्हें <h2></h2> टैग का उपयोग करके प्रस्तुत किया जाना चाहिए।
- शीर्षक की लंबाई 10 शब्दों से कम होनी चाहिए।
- उदाहरण:
/title: न्यूजीलैंड के खिलाफ टेस्ट सीरीज़ को छोड़ने के लिए टास्किन
/content: बांग्लादेश के पेसर टास्किन अहमेद ने कहा कि वह एक बाद के एक शोल्डर चोट के बाद आगामी दो-मैच टेस्ट सीरीज़ के लिए उपलब्ध नहीं होंगे क्योंकि वह अब भी उनकी चोट की व्यायाम शुरू करेंगे और उम्मीद है कि वह दिसंबर में न्यूजीलैंड की यात्रा के दौरान हाथ में होंगे. इसका मतलब है कि टास्किन बांग्लादेश की न्यूजीलैंड की यात्रा की दुसरी टेस्ट समाप्त होने के एक सप्ताह बाद जिसका आयोजन होगा उसके लिए उपलब्ध नहीं होंगे. "मैंने अपने शोल्डर में चोट की तब होने के बाद वहां चोट के साथ खेल रहा था और मेरी सर्वश्रेष्ठ रिदम में नहीं मिला," टास्किन ने कहा. "मैं न्यूजीलैंड के खिलाफ घर पर होने वाले आगामी शीतकाल में टेस्ट सीरीज़ नहीं खेलूंगा क्योंकि मैं थोड़ी देर आराम करके और उम्मीद है कि मैं उनकी यात्रा के बाद न्यूजीलैंड के खिलाड़ियों के साथ T20I के लिए उपलब्ध हो जाऊंगा," उन्होंने कहा कि इससे प्रस्तावित तीन मैच के वनडे सीरीज़ के लिए उपलब्ध नहीं होंगे, जिसके माध्यम से सीरीज़ की शुरुआत होगी.
"""
# gene_model = [CONTENT_GENERATOR, CONTENT_GENERATOR_h2, CONTENT_GENERATOR_HINDI]
def genereate_content(headline, contain, model_check, gene_model):
    content = gene_model.format(headline,contain)
    print("Content is being generated...", end = '')
    completion = openai.ChatCompletion.create(
      model= model_check,
      messages=[
        {"role": "user", "content": content}
      ],
      request_timeout=600
    )
    result = completion.choices[0].message.content.split('/content:')
    ret_title = result[0].strip()
    ret_title = ret_title.split('/title:')[1]
    ret_contain = result[1].strip()
    print("Complete!")
    return ret_title, ret_contain
