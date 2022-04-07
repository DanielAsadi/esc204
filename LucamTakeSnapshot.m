function [snapshot] = LucamTakeSnapshot(cameraNum, filename)
% LucamTakeSnapshot - Takes a snapshot using the predefined settings.
try
    snapshot = LuDispatcher(13, cameraNum);
    writematrix(snapshot, filename);
catch ME
    rethrow(ME);
end
