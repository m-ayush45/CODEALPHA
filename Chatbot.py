import time

def chat_with_bot():
    print("Welcome to the Buddybot! ")
    while True:
        user_input = input("You: ").lower().strip()
        
        if "hello" in user_input:
            print("BuddyBot: Hey there! Good to see you.")
        elif "how are you" in user_input:
            print("BuddyBot: I'm doing great, thanks for asking! How about you?")
        elif "bye" in user_input:
            print("BuddyBot: Catch you later! Take care.")
            break
        elif "what's your name" in user_input:
            print("BuddyBot: I'm BuddyBot, your virtual assistant. What's yours?")
        elif "time" in user_input:
            current_time = time.strftime("%I:%M %p IST, %B %d, %Y")
            print(f"BuddyBot: It's {current_time} right now.")
        elif "good morning" in user_input:
            print("BuddyBot: Good morning! Hope you’ve had your coffee yet.")
        elif "meeting" in user_input:
            print("BuddyBot: Got a meeting? Let me know when, and I’ll set a reminder if you want.")
        elif "deadline" in user_input:
            print("BuddyBot: Oh, deadlines! Need a hand prioritizing? Just let me know.")
        elif "help" in user_input:
            print("BuddyBot: Sure, I’m here to help! What do you need—time, a plan, or just a chat?")
        elif "lunch" in user_input:
            print("BuddyBot: Lunch sounds good! Where are you eating today?")
        elif "what's the plan" in user_input:
            print("BuddyBot: Let’s see… How about we tackle the top task first? What’s on your mind?")
        elif "coffee break" in user_input:
            print("BuddyBot: Perfect timing! I’ll join you virtually with a digital espresso.")
        elif "email" in user_input:
            print("BuddyBot: Need to draft an email? I can suggest a quick template if you like.")
        elif "status" in user_input:
            print("BuddyBot: Status check! How’s your project going? Any updates?")
        elif "good night" in user_input:
            print("BuddyBot: Good night! Rest well, see you tomorrow.")
        else:
            print("BuddyBot: Hmm, not sure I follow. Try 'hello', 'how are you', 'bye', 'what's your name', 'time', 'good morning', 'meeting', 'deadline', 'help', 'lunch', 'what's the plan', 'coffee break', 'email', 'status', or 'good night'.")

if __name__ == "__main__":
    chat_with_bot()