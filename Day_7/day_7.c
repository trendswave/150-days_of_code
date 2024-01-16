/* Define a Node structure for the linked list */
typedef struct Node {
    int data;
    struct Node *next;
} Node;

/* Function to create a new node with the given data */
Node *createNode(int data) {
    Node *newNode = malloc(sizeof(Node));
    if (newNode == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

/* Function to insert a new node at the beginning of the linked list */
void insertAtBeginning(Node **head, int data) {
    Node *newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

/* Function to print the elements of the linked list */
void printList(Node *head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    Node *head = NULL;

    /* Insert some nodes at the beginning */
    insertAtBeginning(&head, 3);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 1);

    /* Print the linked list */
    printf("Linked List: ");
    printList(head);

    return 0;
}
