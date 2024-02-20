# The SignSense Spectacles
### Project for MakeUofT 2024

## Inspiration
Members who have sight loss/are blind or members who are deaf already have solutions to communicate with other people who may not have any impairments. But what about communication amongst each of these respective communities? Given the history of our respective families, the inspiration for the SignSense Spectacles fueled our mission to create a new, innovative piece of technology. The SignSense Spectacles are not just glasses; they're your window to a more accessible, inclusive future.

## What it does
Introducing the SignSense Spectacles – revolutionizing communication for the hard of hearing and visually impaired community.

When conversing with someone fluent in sign language, SignSense Spectacles are your ultimate companion. They read and provide real-time translations using hand gesture recognition models, displayed discreetly within the lenses and via audio feedback, empowering you to engage effortlessly with sign language speakers.

The key note here is the audio feedback! Translating the gestures it detects to audio output now allows for more accessible communication between those who use sign language and people with visual impairments. Of course, these glasses can also be used by anyone trying to learn and understand sign language.

From casual conversations to important meetings, the SignSense Spectacles ensure you never miss a beat. Join us in embracing a world where communication knows no bounds. With SignSense Spectacles, the language of inclusivity is clear for all.

## How we built it
The SignSense Spectacles were built using a combination of different technologies. They are powered by the Qualcomm HDK8450 and the amazing Snapdragon processor. 

## Accomplishments that we're proud of
We chose to bet on the Qualcomm HDK8450 dev kit despite our inexperience with the required stack. Our decision was made on the basis that the Snapdragon 8 was extremely powerful and well-optimized for tasks involving AI, and especially Neural Networks. We're pleased to say that our choice was the correct one, as our sign language detection model runs very smoothly and is extremely accurate. 

Our team also faced numerous external setbacks, with illnesses, transit issues, and inexplicable hardware glitches, but we worked hard and powered through to make sure our project was successful.


## Challenges We Ran into and What We Learned
One challenge we ran into was the Android app development that is needed for the DSP associated with the Qualcomm HDK8450. As all of our members were new to Android development, different alternative routes were used to figure our way around this, but this led to various challenges we know for next time.

To begin, we attempted to load Ubuntu onto the HDK itself so Python scripts could be run. By attending the Qualcomm workshop, we were able to gather knowledge that it was indeed possible but would be quite difficult. We were very close, but rebooting the kit did not end up working.

As a result, we all had to try and learn Android Studio and the Kotlin framework, the industry standard for Android application development. However, learning a new framework, especially in the world of application development, is a hard task to do in under 12 hours. But it is something we tried to learn to complete our project.

Finally, we also connected Wi-Fi/Bluetooth modules to somehow load website applications that were deployed using Wi-Fi. These drivers were a challenge but were finally able to load the Python scripts needed for our project.

## What's next for Us?

Our preliminary project proposal had a secondary facial recognition feature, where the model would be trained to recognize everyone on the user's contacts list. This product would've been catered towards people with prosopagnosia, which is a condition known as face blindness where an individual is unable to see people's faces. It also has a couple other neat use cases, such as Alzheimer's patients who may recognize faces but forget names. We decided to delay this part of our project due to difficulties invoking models within an Android environment.

Additionally, we also wanted to incorporate a text-to-speech model, enabling discrete notifications to avoid any awkward situations. Once again we decided to delay this feature for a later date due to time constraints.

Overall, we are proud of all the deliverables that we were able to meet, and we're excited to see where we can take this next!
