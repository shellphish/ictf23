#include <stdio.h>
#include <stdlib.h>

int main() {
    char username[256];

    // Prompt the user for a username
    printf("Enter a username: ");
    fflush(stdout);
    if (fgets(username, 256, stdin) == NULL) {
        fprintf(stderr, "Failed to read username.\n");
        return 1;
    }

    // Print a message indicating what's about to happen
    printf("Listing process information for users matching: %s\n", username);
    fflush(stdout);

    // Create the command string
    char command[512];
    snprintf(command, sizeof(command), "ps aux | grep ^%s", username);

    // Run the command
    int status = system(command);
    if(status != 0) {
        fprintf(stderr, "Failed to execute command. Exit status: %d\n", status);
        return 1;
    }

    return 0;
}