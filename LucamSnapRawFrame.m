function [frame] = LucamSnapRawFrame(cameraNum)
% LucamSnapRawFrame - Snaps a single frame of raw data.
try
    frame = LuDispatcher(101, cameraNum);
catch ME
    rethrow(ME);
end    
