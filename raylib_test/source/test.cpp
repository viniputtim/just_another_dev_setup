# include <raylib.h>


int main()
{
    InitWindow(0, 0, "Test");
    InitAudioDevice();
    ToggleFullscreen();
    SetMasterVolume(0.5);
    SetTargetFPS(60);

    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawFPS(0, 0);
        EndDrawing();
        InitWindow(width, height, *title)
    }

    CloseWindow();
    CloseAudioDevice();

    return 0;
}
