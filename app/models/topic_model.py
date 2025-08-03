topics = [
    {
        "id": "stack",
        "title": "Stacks",
        "description": "LIFO structure used in compilers, undo, etc.",
        "icon": "📚",
        "learn_content": [
            {
                "heading": "What is a Stack?",
                "text": "A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The most recently added item is removed first."
            },
            {
                "heading": "Core Operations",
                "text": "`push(item)`, `pop()`, `peek()`"
            },
            {
                "heading": "Applications",
                "text": "Used in undo systems, function calls, syntax parsing, and backtracking."
            },
            {
                "heading": "Python Example",
                "text": "```python\nstack = []\nstack.append('a')\nstack.append('b')\nprint(stack.pop())  # b\n```"
            }
        ]
    },
    {
        "id": "queue",
        "title": "Queues",
        "description": "FIFO structure used in scheduling and networks.",
        "icon": "📥",
        "learn_content": [
            {
                "heading": "What is a Queue?",
                "text": "A queue follows the First In First Out (FIFO) principle. The first element added is the first to be removed."
            },
            {
                "heading": "Operations",
                "text": "`enqueue(item)`, `dequeue()`, `peek()`"
            },
            {
                "heading": "Applications",
                "text": "Used in OS scheduling, buffering, and graph traversal (BFS)."
            },
            {
                "heading": "Python Example",
                "text": "```python\nfrom collections import deque\nqueue = deque()\nqueue.append('a')\nqueue.append('b')\nprint(queue.popleft())  # a\n```"
            }
        ]
    },
    {
        "id": "linked_list",
        "title": "Linked Lists",
        "description": "Node-based data structure with flexible memory use.",
        "icon": "🔗",
        "learn_content": [
            {
                "heading": "What is a Linked List?",
                "text": "A collection of nodes, each containing data and a reference to the next node."
            },
            {
                "heading": "Types",
                "text": "Singly, Doubly, Circular linked lists."
            },
            {
                "heading": "Advantages",
                "text": "Dynamic memory, efficient insert/delete."
            },
            {
                "heading": "Python Example",
                "text": "```python\nclass Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\nhead = Node(1)\nhead.next = Node(2)\n```"
            }
        ]
    },
    {
        "id": "hash_map",
        "title": "Hash Maps",
        "description": "Efficient key-value storage. Used in almost everything.",
        "icon": "🗂️",
        "learn_content": [
            {
                "heading": "What is a Hash Map?",
                "text": "A data structure that stores data in key-value pairs using a hash function."
            },
            {
                "heading": "Advantages",
                "text": "Fast lookup, insertion, deletion (average O(1))."
            },
            {
                "heading": "Python Example",
                "text": "```python\nmy_map = {'a': 1, 'b': 2}\nprint(my_map['a'])\n```"
            }
        ]
    },
    {
        "id": "recursion",
        "title": "Recursion",
        "description": "Problem-solving via self-reference.",
        "icon": "🔁",
        "learn_content": [
            {
                "heading": "What is Recursion?",
                "text": "A function that solves a problem by calling itself on smaller inputs."
            },
            {
                "heading": "Structure",
                "text": "Base Case + Recursive Case."
            },
            {
                "heading": "Example",
                "text": "```python\ndef factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n```"
            }
        ]
    },
    {
        "id": "sorting",
        "title": "Sorting Algorithms",
        "description": "Bubble, Merge, Quick, Heap...",
        "icon": "📊",
        "learn_content": [
            {
                "heading": "Common Sorts",
                "text": "Bubble, Merge, Quick, Heap, Insertion."
            },
            {
                "heading": "Efficiency",
                "text": "Merge Sort and Quick Sort are O(n log n)."
            },
            {
                "heading": "Python Example",
                "text": "```python\narr = [4, 1, 3]\narr.sort()\nprint(arr)\n```"
            }
        ]
    },
    {
        "id": "searching",
        "title": "Search Algorithms",
        "description": "Binary, linear, DFS, BFS...",
        "icon": "🔍",
        "learn_content": [
            {
                "heading": "Linear vs Binary",
                "text": "Linear: O(n), Binary: O(log n), requires sorted input."
            },
            {
                "heading": "Graph Search",
                "text": "BFS explores level by level, DFS explores depth."
            },
            {
                "heading": "Python Example",
                "text": "```python\narr = [1, 2, 3, 4]\nif 3 in arr:\n    print(\"Found\")\n```"
            }
        ]
    },
    {
        "id": "os",
        "title": "Operating Systems",
        "description": "Processes, scheduling, memory management.",
        "icon": "🖥️",
        "learn_content": [
            {
                "heading": "Key Concepts",
                "text": "Processes, Threads, Scheduling, Memory Management, File Systems."
            },
            {
                "heading": "Examples",
                "text": "Round Robin scheduling, Paging, Mutex locks."
            }
        ]
    },
    {
        "id": "network",
        "title": "Computer Networks",
        "description": "TCP/IP, HTTP, DNS, protocols.",
        "icon": "🌐",
        "learn_content": [
            {
                "heading": "Layers",
                "text": "Application, Transport, Network, Data Link, Physical."
            },
            {
                "heading": "Protocols",
                "text": "TCP, UDP, IP, HTTP, FTP, DNS."
            }
        ]
    },
    {
        "id": "bash",
        "title": "Bash & CLI",
        "description": "Scripting, file management, piping.",
        "icon": "💻",
        "learn_content": [
            {
                "heading": "Basic Commands",
                "text": "`ls`, `cd`, `touch`, `mkdir`, `rm`, `cat`, `grep`, `find`"
            },
            {
                "heading": "Scripting",
                "text": "#!/bin/bash\necho \"Hello, World!\""
            }
        ]
    },
    {
        "id": "cyber",
        "title": "Cybersecurity",
        "description": "Security concepts, attacks, prevention.",
        "icon": "🛡️",
        "learn_content": [
            {
                "heading": "Concepts",
                "text": "CIA Triad, Authentication, Authorization."
            },
            {
                "heading": "Threats",
                "text": "XSS, SQL Injection, MITM, DoS/DDoS."
            }
        ]
    },
    {
        "id": "ai",
        "title": "Artificial Intelligence",
        "description": "Intro to AI, agents, decision trees.",
        "icon": "🧠",
        "learn_content": [
            {
                "heading": "Subfields",
                "text": "Search, Reasoning, Learning, NLP, Vision."
            },
            {
                "heading": "Agents",
                "text": "Perceive-Think-Act cycle."
            }
        ]
    },
    {
        "id": "ml",
        "title": "Machine Learning",
        "description": "Models, overfitting, regression/classification.",
        "icon": "🤖",
        "learn_content": [
            {
                "heading": "Types",
                "text": "Supervised, Unsupervised, Reinforcement."
            },
            {
                "heading": "Concepts",
                "text": "Features, Labels, Training, Testing."
            }
        ]
    },
    {
        "id": "calculus",
        "title": "Calculus",
        "description": "Derivatives, integrals, limits.",
        "icon": "∫",
        "learn_content": [
            {
                "heading": "Core Ideas",
                "text": "Rate of change (derivatives), Area under curve (integrals)."
            },
            {
                "heading": "Use in CS",
                "text": "Machine learning, physics simulations."
            }
        ]
    },
    {
        "id": "discrete",
        "title": "Discrete Math",
        "description": "Logic, sets, functions, combinatorics.",
        "icon": "📐",
        "learn_content": [
            {
                "heading": "Topics",
                "text": "Propositional logic, truth tables, set theory, graph theory."
            }
        ]
    },
    {
        "id": "linear",
        "title": "Linear Algebra",
        "description": "Vectors, matrices, eigenvalues.",
        "icon": "🧮",
        "learn_content": [
            {
                "heading": "Key Concepts",
                "text": "Matrix multiplication, determinants, vector spaces."
            },
            {
                "heading": "Application",
                "text": "Used heavily in graphics, ML, 3D simulation."
            }
        ]
    },
    {
        "id": "probability",
        "title": "Probability & Stats",
        "description": "Distributions, Bayes, variance.",
        "icon": "🎲",
        "learn_content": [
            {
                "heading": "Probability Rules",
                "text": "Addition, Multiplication, Conditional probability."
            },
            {
                "heading": "Statistics",
                "text": "Mean, Median, Mode, Variance, Standard Deviation."
            }
        ]
    },
    {
        "id": "java",
        "title": "Java",
        "description": "OOP, collections, concurrency.",
        "icon": "☕",
        "learn_content": [
            {
                "heading": "Basics",
                "text": "Classes, Objects, Inheritance, Interfaces."
            },
            {
                "heading": "Java Example",
                "text": "```java\nclass HelloWorld {\n  public static void main(String[] args) {\n    System.out.println(\"Hello\");\n  }\n}```"
            }
        ]
    },
    {
        "id": "python",
        "title": "Python",
        "description": "Syntax, OOP, standard lib, decorators.",
        "icon": "🐍",
        "learn_content": [
            {
                "heading": "Key Features",
                "text": "Dynamic typing, indentation-based, batteries-included."
            },
            {
                "heading": "Example",
                "text": "```python\ndef greet():\n    print(\"Hello\")\ngreet()\n```"
            }
        ]
    }
]




modules = ['learn', 'quiz', 'teach', 'code']
from app import mongo
from bson.objectid import ObjectId
import json

db = mongo.cx['intelligent_tutor']
def get_all_topics(filter_by_name=None):
    query = {}
    if filter_by_name:
        topics = dict(db['themes'].find_one({"name": filter_by_name}))['topics']
        return topics
    topics = list(db['themes'].find(query))
    
    return topics

def get_topic_by_id(topic_id):
    return db['topics'].find_one({"_id": topic_id})
